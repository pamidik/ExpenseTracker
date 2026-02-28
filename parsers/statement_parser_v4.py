"""
BOA Statement Parser - FINAL FIX
Handles multi-line transactions where amount is on next line
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
        
        income_keywords = ['PAYROLL', 'SALARY', 'DEPOSIT', 'DIRECT DEP', 'TRANSFER', 'POLARIS', 'DIGITAL FEDERAL']
        if any(kw in desc_upper for kw in income_keywords):
            return 'Income'
        
        payment_keywords = ['ZELLE', 'PAYMENT', 'PMNT', 'TRANSFER']
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
        """Parse BOA with multi-line transaction support"""
        transactions = []
        
        # Find sections
        text_upper = text.upper()
        deposits_start = text_upper.find('DEPOSITS AND OTHER ADDITIONS')
        withdrawals_start = text_upper.find('WITHDRAWALS AND OTHER SUBTRACTIONS')
        
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
            withdrawals_section = ""
        elif withdrawals_start != -1:
            deposits_section = ""
            withdrawals_section = text[withdrawals_start:]
        else:
            deposits_section = text
            withdrawals_section = ""
        
        # Parse deposits
        if deposits_section:
            txns = self._parse_bofa_multiline(deposits_section, is_deposit=True)
            transactions.extend(txns)
        
        # Parse withdrawals
        if withdrawals_section:
            txns = self._parse_bofa_multiline(withdrawals_section, is_deposit=False)
            transactions.extend(txns)
        
        # Remove duplicates
        seen = set()
        unique = []
        for t in transactions:
            key = (t['date'], t['description'][:30], t['amount'])
            if key not in seen:
                seen.add(key)
                unique.append(t)
        
        unique.sort(key=lambda x: x['date'])
        return unique
    
    def _parse_bofa_multiline(self, text, is_deposit):
        """Parse BOA section handling multi-line transactions"""
        transactions = []
        lines = text.split('\n')
        current_year = datetime.now().year
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Skip empty or header lines
            if not line or len(line) < 5:
                i += 1
                continue
            
            if any(kw in line.upper() for kw in ['DATE', 'DESCRIPTION', 'AMOUNT', 'TOTAL', 'BALANCE', 'CHECKS', 'SERVICE']):
                i += 1
                continue
            
            # Check if line starts with a date
            date_match = re.match(r'^(\d{1,2}/\d{1,2}/\d{2,4})', line)
            
            if date_match:
                date_str = date_match.group(1)
                
                # Get description (everything after date on this line)
                desc_start = date_match.end()
                description = line[desc_start:].strip()
                
                # Look for amount on this line first
                amount_match = re.search(r'([-+]?\$?\s?[\d,]+\.\d{2})\s*$', line)
                
                if amount_match:
                    # Amount is on same line
                    amount_str = amount_match.group(1).replace('$', '').replace(',', '').replace(' ', '').replace('+', '')
                    # Remove amount from description
                    description = line[desc_start:amount_match.start()].strip()
                else:
                    # Amount might be on next line(s)
                    # Look ahead up to 3 lines for amount
                    amount_str = None
                    for j in range(1, min(4, len(lines) - i)):
                        next_line = lines[i + j].strip()
                        # Look for amount at end of line
                        next_amount_match = re.search(r'([-+]?\$?\s?[\d,]+\.\d{2})\s*$', next_line)
                        if next_amount_match:
                            amount_str = next_amount_match.group(1).replace('$', '').replace(',', '').replace(' ', '').replace('+', '')
                            # Append any additional description before amount
                            extra_desc = next_line[:next_amount_match.start()].strip()
                            if extra_desc and not extra_desc.replace(' ', '').isdigit():
                                description += ' ' + extra_desc
                            break
                        else:
                            # This line has more description, add it
                            if next_line and not next_line[0].isdigit():
                                description += ' ' + next_line
                
                # Try to parse if we found both date and amount
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
                        
                        # Parse amount
                        amount = float(amount_str)
                        
                        # Apply sign
                        if is_deposit:
                            amount = abs(amount)
                        else:
                            amount = -abs(amount)
                        
                        # Clean description
                        description = re.sub(r'\s+', ' ', description).strip()
                        description = description[:100]  # Limit length
                        
                        if len(description) > 2:
                            transactions.append({
                                'date': date_obj.strftime('%Y-%m-%d'),
                                'description': description,
                                'amount': amount,
                                'category': self.categorize_transaction(description)
                            })
                    except:
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
