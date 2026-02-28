"""
Enhanced PDF Statement Parser - V3
FIXED: Handles BOA's separate "Deposits" and "Withdrawals" sections
"""

import re
from datetime import datetime
import PyPDF2

class StatementParser:
    def __init__(self):
        self.bank_patterns = {
            'Bank of America': self.parse_bofa,
            'Chase': self.parse_chase,
            'Wells Fargo': self.parse_wells_fargo,
            'DCU': self.parse_dcu,
            '53rd Bank': self.parse_53rd,
            'CIT Bank': self.parse_cit
        }
    
    def detect_bank(self, text):
        """Detect which bank the statement is from"""
        text_upper = text.upper()
        
        if 'BANK OF AMERICA' in text_upper or 'BANKOFAMERICA' in text_upper:
            return 'Bank of America'
        elif 'CHASE' in text_upper or 'JPMORGAN' in text_upper:
            return 'Chase'
        elif 'WELLS FARGO' in text_upper:
            return 'Wells Fargo'
        elif 'DCU' in text_upper or 'DIGITAL FEDERAL' in text_upper:
            return 'DCU'
        elif '53' in text_upper and ('BANK' in text_upper or 'FIFTH THIRD' in text_upper):
            return '53rd Bank'
        elif 'CIT BANK' in text_upper:
            return 'CIT Bank'
        
        return 'Unknown'
    
    def categorize_transaction(self, description):
        """Auto-categorize based on merchant name"""
        desc_upper = description.upper()
        
        food_keywords = ['RESTAURANT', 'CAFE', 'COFFEE', 'STARBUCKS', 'MCDONALD', 
                        'BURGER', 'PIZZA', 'DINE', 'FOOD', 'GROCERY', 'WHOLE FOODS',
                        'WALMART', 'TARGET', 'COSTCO', 'KROGER', 'SAFEWAY', 'PUBLIX']
        if any(kw in desc_upper for kw in food_keywords):
            return 'Food & Dining'
        
        gas_keywords = ['GAS', 'EXXON', 'SHELL', 'CHEVRON', 'MOBIL', 'BP', 'FUEL', 'PETRO']
        if any(kw in desc_upper for kw in gas_keywords):
            return 'Gas & Auto'
        
        shopping_keywords = ['AMAZON', 'EBAY', 'STORE', 'SHOP', 'MALL', 'RETAIL']
        if any(kw in desc_upper for kw in shopping_keywords):
            return 'Shopping'
        
        entertainment_keywords = ['NETFLIX', 'SPOTIFY', 'HULU', 'DISNEY', 'MOVIE', 
                                 'THEATER', 'GAME', 'ENTERTAINMENT', 'PRIME VIDEO']
        if any(kw in desc_upper for kw in entertainment_keywords):
            return 'Entertainment'
        
        utility_keywords = ['ELECTRIC', 'WATER', 'GAS COMPANY', 'UTILITY', 'INTERNET',
                           'PHONE', 'WIRELESS', 'CABLE', 'AT&T', 'VERIZON', 'T-MOBILE']
        if any(kw in desc_upper for kw in utility_keywords):
            return 'Utilities'
        
        health_keywords = ['PHARMACY', 'CVS', 'WALGREENS', 'MEDICAL', 'DOCTOR', 
                          'HOSPITAL', 'HEALTH', 'DENTAL', 'CLINIC']
        if any(kw in desc_upper for kw in health_keywords):
            return 'Healthcare'
        
        income_keywords = ['PAYROLL', 'SALARY', 'DEPOSIT', 'DIRECT DEP', 'TRANSFER IN', 
                          'PAYMENT RECEIVED', 'ACH CREDIT', 'DIRECT CREDIT']
        if any(kw in desc_upper for kw in income_keywords):
            return 'Income'
        
        return 'Other'
    
    def parse_pdf(self, pdf_file):
        """Main parsing function"""
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text() + '\n'
            
            bank = self.detect_bank(text)
            
            if bank == 'Unknown':
                return {
                    'success': False,
                    'message': 'Unable to detect bank format'
                }
            
            parser_func = self.bank_patterns.get(bank)
            transactions = parser_func(text)
            
            total_income = sum(t['amount'] for t in transactions if t['amount'] > 0)
            total_expenses = sum(abs(t['amount']) for t in transactions if t['amount'] < 0)
            
            return {
                'success': True,
                'bank': bank,
                'transactions': transactions,
                'total_income': total_income,
                'total_expenses': total_expenses,
                'count': len(transactions)
            }
            
        except Exception as e:
            return {
                'success': False,
                'message': f'Error: {str(e)}'
            }
    
    def parse_bofa(self, text):
        """Parse Bank of America - Handles BOTH Deposits and Withdrawals sections"""
        transactions = []
        
        # Split text into sections
        # Look for section headers
        deposits_section = ""
        withdrawals_section = ""
        
        # Try to find the sections
        text_upper = text.upper()
        
        # Find deposits section
        deposits_start = -1
        deposits_keywords = ['DEPOSITS AND OTHER ADDITIONS', 'DEPOSITS AND ADDITIONS', 
                            'DEPOSITS', 'CREDITS AND OTHER ADDITIONS']
        for keyword in deposits_keywords:
            idx = text_upper.find(keyword)
            if idx != -1:
                deposits_start = idx
                break
        
        # Find withdrawals section
        withdrawals_start = -1
        withdrawals_keywords = ['WITHDRAWALS AND OTHER SUBTRACTIONS', 'WITHDRAWALS AND SUBTRACTIONS',
                               'WITHDRAWALS', 'DEBITS AND OTHER SUBTRACTIONS', 'CHECKS']
        for keyword in withdrawals_keywords:
            idx = text_upper.find(keyword)
            if idx != -1:
                withdrawals_start = idx
                break
        
        # Extract sections
        if deposits_start != -1 and withdrawals_start != -1:
            if deposits_start < withdrawals_start:
                deposits_section = text[deposits_start:withdrawals_start]
                withdrawals_section = text[withdrawals_start:]
            else:
                deposits_section = text[deposits_start:]
                withdrawals_section = text[withdrawals_start:deposits_start]
        elif deposits_start != -1:
            deposits_section = text[deposits_start:]
        elif withdrawals_start != -1:
            withdrawals_section = text[withdrawals_start:]
        else:
            # No sections found, parse entire text
            deposits_section = text
            withdrawals_section = text
        
        # Parse deposits (positive amounts)
        if deposits_section:
            deposit_txns = self._parse_bofa_section(deposits_section, is_deposit=True)
            transactions.extend(deposit_txns)
        
        # Parse withdrawals (negative amounts)
        if withdrawals_section:
            withdrawal_txns = self._parse_bofa_section(withdrawals_section, is_deposit=False)
            transactions.extend(withdrawal_txns)
        
        # If we still have no transactions, try parsing the whole document without sections
        if len(transactions) == 0:
            transactions = self._parse_bofa_section(text, is_deposit=None)
        
        # Remove duplicates
        seen = set()
        unique_transactions = []
        for t in transactions:
            key = (t['date'], t['description'], t['amount'])
            if key not in seen:
                seen.add(key)
                unique_transactions.append(t)
        
        # Sort by date
        unique_transactions.sort(key=lambda x: x['date'])
        
        return unique_transactions
    
    def _parse_bofa_section(self, text, is_deposit):
        """Parse a BOA section (deposits or withdrawals)"""
        transactions = []
        lines = text.split('\n')
        current_year = datetime.now().year
        
        # Regex patterns for different BOA formats
        patterns = [
            # Pattern 1: Date Description Amount (flexible spacing)
            r'(\d{1,2}/\d{1,2}(?:/\d{2,4})?)\s+(.+?)\s+([-+]?\$?\s?[\d,]+\.\d{2})\s*$',
            
            # Pattern 2: Date Description Amount (multiple spaces)
            r'(\d{1,2}/\d{1,2}(?:/\d{2,4})?)\s{2,}(.+?)\s{2,}([-+]?\$?\s?[\d,]+\.\d{2})',
            
            # Pattern 3: More flexible - anything with date and amount
            r'(\d{1,2}/\d{1,2}(?:/\d{2,4})?)\s+(.+?)\s+([\d,]+\.\d{2})',
        ]
        
        for line in lines:
            line = line.strip()
            if not line or len(line) < 10:
                continue
            
            # Skip header lines
            if any(keyword in line.upper() for keyword in ['BALANCE', 'TOTAL', 'ENDING', 'BEGINNING', 'DATE', 'DESCRIPTION', 'AMOUNT']):
                continue
            
            matched = False
            for pattern in patterns:
                match = re.search(pattern, line)
                if match:
                    try:
                        date_str = match.group(1)
                        description = match.group(2).strip()
                        amount_str = match.group(3).replace('$', '').replace(',', '').replace(' ', '').replace('+', '')
                        
                        # Validate description (must be more than just numbers/symbols)
                        if len(description) < 3 or description.replace(' ', '').replace('-', '').replace('.', '').isdigit():
                            continue
                        
                        # Skip if description is a balance or total
                        if any(keyword in description.upper() for keyword in ['BALANCE', 'TOTAL', 'SUBTOTAL']):
                            continue
                        
                        # Parse date
                        parts = date_str.split('/')
                        if len(parts) == 2:
                            date_obj = datetime.strptime(f'{date_str}/{current_year}', '%m/%d/%Y')
                        elif len(parts) == 3:
                            if len(parts[2]) == 2:
                                date_obj = datetime.strptime(date_str, '%m/%d/%y')
                            else:
                                date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                        else:
                            continue
                        
                        # Parse amount
                        try:
                            amount = float(amount_str)
                        except:
                            continue
                        
                        # Apply sign based on section
                        if is_deposit is True:
                            # Deposits are always positive
                            amount = abs(amount)
                        elif is_deposit is False:
                            # Withdrawals are always negative
                            amount = -abs(amount)
                        else:
                            # Unknown section - check if amount already has sign
                            # If no sign in original, assume withdrawal
                            if '-' not in match.group(3):
                                amount = -abs(amount)
                        
                        transactions.append({
                            'date': date_obj.strftime('%Y-%m-%d'),
                            'description': description,
                            'amount': amount,
                            'category': self.categorize_transaction(description)
                        })
                        
                        matched = True
                        break  # Found a match, stop trying patterns
                        
                    except Exception as e:
                        continue
            
            # If no pattern matched but line has date and amount, try extracting manually
            if not matched:
                date_match = re.search(r'\d{1,2}/\d{1,2}(?:/\d{2,4})?', line)
                amount_match = re.search(r'[\d,]+\.\d{2}', line)
                
                if date_match and amount_match:
                    try:
                        date_str = date_match.group()
                        amount_str = amount_match.group().replace(',', '')
                        
                        # Description is between date and amount
                        desc_start = date_match.end()
                        desc_end = amount_match.start()
                        description = line[desc_start:desc_end].strip()
                        
                        # Clean description (remove extra spaces, dollar signs)
                        description = re.sub(r'\s+', ' ', description)
                        description = description.replace('$', '').strip()
                        
                        if len(description) > 2 and not description.replace(' ', '').isdigit():
                            # Parse date
                            parts = date_str.split('/')
                            if len(parts) == 2:
                                date_obj = datetime.strptime(f'{date_str}/{current_year}', '%m/%d/%Y')
                            elif len(parts) == 3:
                                if len(parts[2]) == 2:
                                    date_obj = datetime.strptime(date_str, '%m/%d/%y')
                                else:
                                    date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                            else:
                                continue
                            
                            amount = float(amount_str)
                            
                            # Apply sign based on section
                            if is_deposit is True:
                                amount = abs(amount)
                            elif is_deposit is False:
                                amount = -abs(amount)
                            else:
                                amount = -abs(amount)  # Default to withdrawal
                            
                            transactions.append({
                                'date': date_obj.strftime('%Y-%m-%d'),
                                'description': description,
                                'amount': amount,
                                'category': self.categorize_transaction(description)
                            })
                    except:
                        continue
        
        return transactions
    
    def parse_chase(self, text):
        """Parse Chase statement"""
        transactions = []
        lines = text.split('\n')
        current_year = datetime.now().year
        
        for line in lines:
            match = re.search(r'(\d{1,2}/\d{1,2})\s+(.+?)\s+([-+]?\$?[\d,]+\.\d{2})', line)
            if match:
                try:
                    date_str = match.group(1)
                    description = match.group(2).strip()
                    amount_str = match.group(3).replace('$', '').replace(',', '')
                    
                    if len(description) > 2:
                        date_obj = datetime.strptime(f'{date_str}/{current_year}', '%m/%d/%Y')
                        amount = float(amount_str)
                        
                        transactions.append({
                            'date': date_obj.strftime('%Y-%m-%d'),
                            'description': description,
                            'amount': amount,
                            'category': self.categorize_transaction(description)
                        })
                except:
                    continue
        
        return transactions
    
    def parse_wells_fargo(self, text):
        """Parse Wells Fargo statement"""
        transactions = []
        lines = text.split('\n')
        
        for line in lines:
            match = re.search(r'(\d{1,2}/\d{1,2}/\d{2})\s+(.+?)\s+([-+]?\$?[\d,]+\.\d{2})', line)
            if match:
                try:
                    date_str = match.group(1)
                    description = match.group(2).strip()
                    amount_str = match.group(3).replace('$', '').replace(',', '')
                    
                    if len(description) > 2:
                        date_obj = datetime.strptime(date_str, '%m/%d/%y')
                        amount = float(amount_str)
                        
                        transactions.append({
                            'date': date_obj.strftime('%Y-%m-%d'),
                            'description': description,
                            'amount': amount,
                            'category': self.categorize_transaction(description)
                        })
                except:
                    continue
        
        return transactions
    
    def parse_dcu(self, text):
        """Parse DCU statement"""
        transactions = []
        lines = text.split('\n')
        
        for line in lines:
            match = re.search(r'(\d{1,2}/\d{1,2}/\d{4})\s+(.+?)\s+([-+]?\$?[\d,]+\.\d{2})', line)
            if match:
                try:
                    date_str = match.group(1)
                    description = match.group(2).strip()
                    amount_str = match.group(3).replace('$', '').replace(',', '')
                    
                    if len(description) > 2:
                        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                        amount = float(amount_str)
                        
                        transactions.append({
                            'date': date_obj.strftime('%Y-%m-%d'),
                            'description': description,
                            'amount': amount,
                            'category': self.categorize_transaction(description)
                        })
                except:
                    continue
        
        return transactions
    
    def parse_53rd(self, text):
        """Parse 53rd Bank statement"""
        transactions = []
        lines = text.split('\n')
        
        for line in lines:
            match = re.search(r'(\d{1,2}/\d{1,2}/\d{2})\s+(.+?)\s+([-+]?\$?[\d,]+\.\d{2})', line)
            if match:
                try:
                    date_str = match.group(1)
                    description = match.group(2).strip()
                    amount_str = match.group(3).replace('$', '').replace(',', '')
                    
                    if len(description) > 2:
                        date_obj = datetime.strptime(date_str, '%m/%d/%y')
                        amount = float(amount_str)
                        
                        transactions.append({
                            'date': date_obj.strftime('%Y-%m-%d'),
                            'description': description,
                            'amount': amount,
                            'category': self.categorize_transaction(description)
                        })
                except:
                    continue
        
        return transactions
    
    def parse_cit(self, text):
        """Parse CIT Bank statement"""
        transactions = []
        lines = text.split('\n')
        
        for line in lines:
            match = re.search(r'(\d{4}-\d{2}-\d{2})\s+(.+?)\s+([-+]?\$?[\d,]+\.\d{2})', line)
            if not match:
                match = re.search(r'(\d{1,2}/\d{1,2}/\d{4})\s+(.+?)\s+([-+]?\$?[\d,]+\.\d{2})', line)
            
            if match:
                try:
                    date_str = match.group(1)
                    description = match.group(2).strip()
                    amount_str = match.group(3).replace('$', '').replace(',', '')
                    
                    if len(description) > 2:
                        if '-' in date_str:
                            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
                        else:
                            date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                        
                        amount = float(amount_str)
                        
                        transactions.append({
                            'date': date_obj.strftime('%Y-%m-%d'),
                            'description': description,
                            'amount': amount,
                            'category': self.categorize_transaction(description)
                        })
                except:
                    continue
        
        return transactions


# Initialize parser
parser = StatementParser()
