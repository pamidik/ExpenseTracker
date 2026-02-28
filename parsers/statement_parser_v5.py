"""
BOA Statement Parser - FIXED
Properly handles deposits as positive and withdrawals as negative
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
        desc_upper = description.upper()
        
        food_keywords = ['RESTAURANT', 'CAFE', 'COFFEE', 'STARBUCKS', 'MCDONALD', 
                        'BURGER', 'PIZZA', 'FOOD', 'GROCERY', 'WALMART', 'TARGET', 'COSTCO', 'PUBLIX']
        if any(kw in desc_upper for kw in food_keywords):
            return 'Food & Dining'
        
        gas_keywords = ['GAS', 'EXXON', 'SHELL', 'CHEVRON', 'MOBIL', 'BP', 'FUEL']
        if any(kw in desc_upper for kw in gas_keywords):
            return 'Gas & Auto'
        
        shopping_keywords = ['AMAZON', 'EBAY', 'STORE', 'SHOP', 'MALL']
        if any(kw in desc_upper for kw in shopping_keywords):
            return 'Shopping'
        
        entertainment_keywords = ['NETFLIX', 'SPOTIFY', 'HULU', 'DISNEY', 'MOVIE', 'GAME']
        if any(kw in desc_upper for kw in entertainment_keywords):
            return 'Entertainment'
        
        utility_keywords = ['ELECTRIC', 'WATER', 'UTILITY', 'INTERNET', 'PHONE', 'WIRELESS', 'CABLE']
        if any(kw in desc_upper for kw in utility_keywords):
            return 'Utilities'
        
        health_keywords = ['PHARMACY', 'CVS', 'WALGREENS', 'MEDICAL', 'DOCTOR', 'HOSPITAL', 'DENTAL']
        if any(kw in desc_upper for kw in health_keywords):
            return 'Healthcare'
        
        income_keywords = ['PAYROLL', 'SALARY', 'DEPOSIT', 'DIRECT DEP', 'POLARIS']
        if any(kw in desc_upper for kw in income_keywords):
            return 'Income'
        
        payment_keywords = ['ZELLE', 'PAYMENT', 'PMNT']
        if any(kw in desc_upper for kw in payment_keywords):
            return 'Transfers & Payments'
        
        return 'Other'
    
    def parse_pdf(self, pdf_file):
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text() + '\n'
            
            bank = self.detect_bank(text)
            if bank == 'Unknown':
                return {'success': False, 'message': 'Unable to detect bank format'}
            
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
            return {'success': False, 'message': f'Error: {str(e)}'}
    
    def parse_bofa(self, text):
        """Parse BOA - Split into deposits and withdrawals sections"""
        transactions = []
        
        # Split into sections
        text_upper = text.upper()
        
        # Find section markers
        deposits_idx = text_upper.find('DEPOSITS AND OTHER ADDITIONS')
        withdrawals_idx = text_upper.find('WITHDRAWALS AND OTHER SUBTRACTIONS')
        
        print(f"DEBUG: deposits_idx={deposits_idx}, withdrawals_idx={withdrawals_idx}")
        
        # Extract sections
        deposits_section = ""
        withdrawals_section = ""
        
        if deposits_idx != -1 and withdrawals_idx != -1:
            # Both sections exist
            if deposits_idx < withdrawals_idx:
                # Deposits comes first
                deposits_section = text[deposits_idx:withdrawals_idx]
                # Find end of withdrawals (look for "Total" or end of document)
                end_markers = ['TOTAL WITHDRAWALS', 'CHECKS', 'SERVICE FEES', 'ENDING BALANCE']
                withdrawals_end = len(text)
                for marker in end_markers:
                    idx = text_upper.find(marker, withdrawals_idx + 100)
                    if idx != -1 and idx < withdrawals_end:
                        withdrawals_end = idx
                withdrawals_section = text[withdrawals_idx:withdrawals_end]
            else:
                # Withdrawals comes first (unusual but handle it)
                withdrawals_section = text[withdrawals_idx:deposits_idx]
                deposits_section = text[deposits_idx:]
        elif deposits_idx != -1:
            # Only deposits section found
            deposits_section = text[deposits_idx:]
        elif withdrawals_idx != -1:
            # Only withdrawals section found
            withdrawals_section = text[withdrawals_idx:]
        
        print(f"DEBUG: deposits_section length={len(deposits_section)}")
        print(f"DEBUG: withdrawals_section length={len(withdrawals_section)}")
        
        # Parse deposits as POSITIVE amounts
        if deposits_section:
            print("DEBUG: Parsing deposits section...")
            deposit_txns = self._parse_bofa_section(deposits_section, section_type='DEPOSIT')
            print(f"DEBUG: Found {len(deposit_txns)} deposit transactions")
            transactions.extend(deposit_txns)
        
        # Parse withdrawals as NEGATIVE amounts
        if withdrawals_section:
            print("DEBUG: Parsing withdrawals section...")
            withdrawal_txns = self._parse_bofa_section(withdrawals_section, section_type='WITHDRAWAL')
            print(f"DEBUG: Found {len(withdrawal_txns)} withdrawal transactions")
            transactions.extend(withdrawal_txns)
        
        # Remove duplicates
        seen = set()
        unique = []
        for t in transactions:
            key = (t['date'], t['description'][:30], abs(t['amount']))
            if key not in seen:
                seen.add(key)
                unique.append(t)
        
        unique.sort(key=lambda x: x['date'])
        
        print(f"DEBUG: Total unique transactions={len(unique)}")
        return unique
    
    def _parse_bofa_section(self, text, section_type):
        """
        Parse a BOA section (DEPOSIT or WITHDRAWAL)
        section_type: 'DEPOSIT' or 'WITHDRAWAL'
        """
        transactions = []
        lines = text.split('\n')
        current_year = datetime.now().year
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty lines
            if not line or len(line) < 5:
                i += 1
                continue
            
            # Skip header lines
            line_upper = line.upper()
            if any(kw in line_upper for kw in ['DATE', 'DESCRIPTION', 'AMOUNT', 'TOTAL', 'BALANCE', 'CHECKS', 'SERVICE', 'ENDING', 'BEGINNING']):
                i += 1
                continue
            
            # Check if line starts with a date pattern
            date_match = re.match(r'^(\d{1,2}/\d{1,2}/\d{2,4})', line)
            
            if date_match:
                date_str = date_match.group(1)
                
                # Everything after date is description
                desc_start = date_match.end()
                description = line[desc_start:].strip()
                
                # Look for amount on THIS line
                amount_match = re.search(r'([-+]?\$?\s?[\d,]+\.\d{2})\s*$', line)
                
                amount_str = None
                if amount_match:
                    # Amount is on same line
                    amount_str = amount_match.group(1)
                    # Remove amount from description
                    description = line[desc_start:amount_match.start()].strip()
                else:
                    # Amount might be on next line(s)
                    # Look ahead up to 3 lines
                    for j in range(1, min(4, len(lines) - i)):
                        next_line = lines[i + j].strip()
                        if not next_line:
                            continue
                        
                        # Check if this line has an amount at the end
                        next_amount_match = re.search(r'([-+]?\$?\s?[\d,]+\.\d{2})\s*$', next_line)
                        if next_amount_match:
                            amount_str = next_amount_match.group(1)
                            # Add any extra description before the amount
                            extra_desc = next_line[:next_amount_match.start()].strip()
                            if extra_desc and not extra_desc.replace(' ', '').replace('-', '').isdigit():
                                description += ' ' + extra_desc
                            break
                        else:
                            # This line might be continuation of description
                            # Only add if it doesn't start with a date
                            if not re.match(r'^\d{1,2}/\d{1,2}', next_line):
                                description += ' ' + next_line
                
                # Try to create transaction if we found both date and amount
                if amount_str:
                    try:
                        # Parse date
                        parts = date_str.split('/')
                        if len(parts) == 3:
                            if len(parts[2]) == 2:
                                date_obj = datetime.strptime(date_str, '%m/%d/%y')
                            else:
                                date_obj = datetime.strptime(date_str, '%m/%d/%Y')
                        else:
                            date_obj = datetime.strptime(f'{date_str}/{current_year}', '%m/%d/%Y')
                        
                        # Clean and parse amount
                        amount_clean = amount_str.replace('$', '').replace(',', '').replace(' ', '').replace('+', '')
                        # Remove any minus sign from the string (we'll apply sign based on section)
                        amount_clean = amount_clean.replace('-', '')
                        amount = float(amount_clean)
                        
                        # Apply sign based on section type
                        if section_type == 'DEPOSIT':
                            # Deposits are ALWAYS positive
                            amount = abs(amount)
                            print(f"DEBUG DEPOSIT: {date_str} | {description[:30]} | +${amount}")
                        elif section_type == 'WITHDRAWAL':
                            # Withdrawals are ALWAYS negative
                            amount = -abs(amount)
                            print(f"DEBUG WITHDRAWAL: {date_str} | {description[:30]} | -${abs(amount)}")
                        
                        # Clean description
                        description = re.sub(r'\s+', ' ', description).strip()
                        description = description[:150]
                        
                        if len(description) > 2:
                            transactions.append({
                                'date': date_obj.strftime('%Y-%m-%d'),
                                'description': description,
                                'amount': amount,
                                'category': self.categorize_transaction(description)
                            })
                    except Exception as e:
                        print(f"DEBUG ERROR parsing: {line} | Error: {e}")
                        pass
            
            i += 1
        
        return transactions
    
    def parse_chase(self, text):
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


parser = StatementParser()
