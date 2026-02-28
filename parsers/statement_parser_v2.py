"""
Enhanced PDF Statement Parser - Works with Multiple Formats
Supports: Bank of America, Chase, Wells Fargo, DCU, 53rd Bank, CIT Bank
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
        
        income_keywords = ['PAYROLL', 'SALARY', 'DEPOSIT', 'DIRECT DEP', 'TRANSFER IN', 'PAYMENT RECEIVED']
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
        """Parse Bank of America - Multiple pattern support"""
        transactions = []
        lines = text.split('\n')
        
        # Try multiple BOA formats
        patterns = [
            # Format 1: Date Description Amount (space separated)
            r'(\d{1,2}/\d{1,2}(?:/\d{2,4})?)\s+(.+?)\s+([-+]?\$?[\d,]+\.\d{2})\s*$',
            
            # Format 2: Date on own line, description next, amount last
            r'(\d{1,2}/\d{1,2}(?:/\d{2,4})?)',
            
            # Format 3: Tab or multiple space separated
            r'(\d{1,2}/\d{1,2}(?:/\d{2,4})?)\s{2,}(.+?)\s{2,}([-+]?\$?[\d,]+\.\d{2})',
        ]
        
        current_year = datetime.now().year
        
        # Method 1: Try direct pattern matching
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            for pattern in patterns:
                matches = re.finditer(pattern, line)
                for match in matches:
                    try:
                        groups = match.groups()
                        if len(groups) >= 3:
                            date_str = groups[0]
                            description = groups[1].strip()
                            amount_str = groups[2].replace('$', '').replace(',', '').replace('+', '')
                            
                            # Skip if description is too short or amount is invalid
                            if len(description) < 3:
                                continue
                            
                            # Parse date
                            if '/' in date_str:
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
                            else:
                                continue
                            
                            # Parse amount
                            amount = float(amount_str)
                            
                            # BOA typically shows withdrawals as negative
                            
                            transactions.append({
                                'date': date_obj.strftime('%Y-%m-%d'),
                                'description': description,
                                'amount': amount,
                                'category': self.categorize_transaction(description)
                            })
                            break  # Found valid transaction, move to next line
                    except:
                        continue
        
        # Method 2: Look for transaction sections with headers
        if len(transactions) == 0:
            # Find lines with dates and amounts
            date_pattern = r'\d{1,2}/\d{1,2}(?:/\d{2,4})?'
            amount_pattern = r'[-+]?\$?[\d,]+\.\d{2}'
            
            for i, line in enumerate(lines):
                if re.search(date_pattern, line) and re.search(amount_pattern, line):
                    # This line has both date and amount
                    parts = line.split()
                    
                    # Try to extract date (first part)
                    date_match = re.search(date_pattern, line)
                    amount_match = re.search(amount_pattern, line)
                    
                    if date_match and amount_match:
                        date_str = date_match.group()
                        amount_str = amount_match.group().replace('$', '').replace(',', '')
                        
                        # Description is everything between date and amount
                        desc_start = date_match.end()
                        desc_end = amount_match.start()
                        description = line[desc_start:desc_end].strip()
                        
                        if len(description) > 2:
                            try:
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
                                
                                transactions.append({
                                    'date': date_obj.strftime('%Y-%m-%d'),
                                    'description': description,
                                    'amount': amount,
                                    'category': self.categorize_transaction(description)
                                })
                            except:
                                continue
        
        # Remove duplicates
        seen = set()
        unique_transactions = []
        for t in transactions:
            key = (t['date'], t['description'], t['amount'])
            if key not in seen:
                seen.add(key)
                unique_transactions.append(t)
        
        return unique_transactions
    
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
            # Try YYYY-MM-DD format first
            match = re.search(r'(\d{4}-\d{2}-\d{2})\s+(.+?)\s+([-+]?\$?[\d,]+\.\d{2})', line)
            if not match:
                # Try MM/DD/YYYY format
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
