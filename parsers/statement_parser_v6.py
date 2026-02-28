"""
BOA Statement Parser - WORKING VERSION
Based on actual BOA statement format with amounts in right column
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
        
        health_keywords = ['PHARMACY', 'CVS', 'WALGREENS', 'MEDICAL', 'DOCTOR', 'HOSPITAL', 'DENTAL', 'ACADEMY']
        if any(kw in desc_upper for kw in health_keywords):
            return 'Healthcare'
        
        income_keywords = ['PAYROLL', 'SALARY', 'POLARIS']
        if any(kw in desc_upper for kw in income_keywords):
            return 'Income'
        
        transfer_keywords = ['ZELLE', 'PMNT SENT', 'ONLINE BANKING PAYMENT', 'TRANSFER', 'DIGITAL FEDERAL']
        if any(kw in desc_upper for kw in transfer_keywords):
            return 'Transfers & Payments'
        
        credit_keywords = ['AMERICAN EXPRESS', 'CHASE CREDIT', 'CREDIT CARD']
        if any(kw in desc_upper for kw in credit_keywords):
            return 'Credit Card Payment'
        
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
        """
        Parse BOA statement based on actual format:
        - Amounts are in right column
        - Deposits section = positive
        - Withdrawals section = negative
        """
        transactions = []
        lines = text.split('\n')
        
        # Track which section we're in
        in_deposits = False
        in_withdrawals = False
        current_year = datetime.now().year
        
        # Current transaction being built
        current_date = None
        current_description = ""
        
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue
            
            line_upper = line.upper()
            
            # Check for section headers
            if 'DEPOSITS AND OTHER ADDITIONS' in line_upper:
                in_deposits = True
                in_withdrawals = False
                continue
            elif 'WITHDRAWALS AND OTHER SUBTRACTIONS' in line_upper:
                in_deposits = False
                in_withdrawals = True
                continue
            elif 'TOTAL DEPOSITS' in line_upper or 'TOTAL WITHDRAWALS' in line_upper:
                # End of section
                in_deposits = False
                in_withdrawals = False
                continue
            
            # Skip header lines
            if any(kw in line_upper for kw in ['DATE', 'DESCRIPTION', 'AMOUNT', 'CHECKS', 'SERVICE FEES', 'ENDING BALANCE', 'BEGINNING BALANCE']):
                continue
            
            # Only process if we're in a section
            if not (in_deposits or in_withdrawals):
                continue
            
            # Check if line starts with a date
            date_match = re.match(r'^(\d{1,2}/\d{1,2}/\d{2,4})', line)
            
            if date_match:
                # Save previous transaction if exists
                if current_date and current_description:
                    # This shouldn't happen, but just in case
                    pass
                
                # Start new transaction
                current_date = date_match.group(1)
                # Everything after date is description
                rest_of_line = line[date_match.end():].strip()
                
                # Check if amount is on THIS line (look for number at the end)
                amount_match = re.search(r'([-]?[\d,]+\.\d{2})\s*$', rest_of_line)
                
                if amount_match:
                    # Complete transaction on one line
                    amount_str = amount_match.group(1).replace(',', '')
                    description = rest_of_line[:amount_match.start()].strip()
                    
                    # Create transaction
                    try:
                        # Parse date
                        parts = current_date.split('/')
                        if len(parts) == 3:
                            if len(parts[2]) == 2:
                                date_obj = datetime.strptime(current_date, '%m/%d/%y')
                            else:
                                date_obj = datetime.strptime(current_date, '%m/%d/%Y')
                        else:
                            date_obj = datetime.strptime(f'{current_date}/{current_year}', '%m/%d/%Y')
                        
                        # Parse amount and apply sign
                        amount = float(amount_str)
                        if in_deposits:
                            amount = abs(amount)  # Deposits are positive
                        else:
                            amount = -abs(amount)  # Withdrawals are negative
                        
                        if len(description) > 2:
                            transactions.append({
                                'date': date_obj.strftime('%Y-%m-%d'),
                                'description': description,
                                'amount': amount,
                                'category': self.categorize_transaction(description)
                            })
                    except Exception as e:
                        pass
                    
                    # Reset
                    current_date = None
                    current_description = ""
                else:
                    # Multi-line transaction - description continues
                    current_description = rest_of_line
            
            elif current_date:
                # Continuation of multi-line transaction
                # Check if this line has the amount
                amount_match = re.search(r'([-]?[\d,]+\.\d{2})\s*$', line)
                
                if amount_match:
                    # Found the amount - complete the transaction
                    amount_str = amount_match.group(1).replace(',', '')
                    extra_desc = line[:amount_match.start()].strip()
                    if extra_desc:
                        current_description += ' ' + extra_desc
                    
                    # Create transaction
                    try:
                        # Parse date
                        parts = current_date.split('/')
                        if len(parts) == 3:
                            if len(parts[2]) == 2:
                                date_obj = datetime.strptime(current_date, '%m/%d/%y')
                            else:
                                date_obj = datetime.strptime(current_date, '%m/%d/%Y')
                        else:
                            date_obj = datetime.strptime(f'{current_date}/{current_year}', '%m/%d/%Y')
                        
                        # Parse amount and apply sign
                        amount = float(amount_str)
                        if in_deposits:
                            amount = abs(amount)  # Deposits are positive
                        else:
                            amount = -abs(amount)  # Withdrawals are negative
                        
                        # Clean description
                        current_description = re.sub(r'\s+', ' ', current_description).strip()
                        
                        if len(current_description) > 2:
                            transactions.append({
                                'date': date_obj.strftime('%Y-%m-%d'),
                                'description': current_description[:200],
                                'amount': amount,
                                'category': self.categorize_transaction(current_description)
                            })
                    except Exception as e:
                        pass
                    
                    # Reset
                    current_date = None
                    current_description = ""
                else:
                    # More description
                    current_description += ' ' + line
        
        # Remove duplicates
        seen = set()
        unique = []
        for t in transactions:
            key = (t['date'], t['description'][:50], abs(t['amount']))
            if key not in seen:
                seen.add(key)
                unique.append(t)
        
        unique.sort(key=lambda x: x['date'])
        return unique
    
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
