"""
Statement Parser Test Script
This will help diagnose your BOA statement format
"""

import PyPDF2
import sys

def test_statement(pdf_path):
    """Extract and show raw text from PDF"""
    print("="*80)
    print("STATEMENT TEXT EXTRACTION TEST")
    print("="*80)
    
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            
            print(f"\nTotal pages: {len(pdf_reader.pages)}")
            print("="*80)
            
            all_text = ""
            for i, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                all_text += page_text + "\n"
                
                print(f"\n--- PAGE {i+1} ---")
                print(page_text[:1000])  # Show first 1000 chars
                print("...")
            
            print("\n" + "="*80)
            print("SEARCHING FOR KEY SECTIONS")
            print("="*80)
            
            text_upper = all_text.upper()
            
            # Check for deposits section
            if 'DEPOSITS' in text_upper:
                print("✓ Found 'DEPOSITS' section")
                idx = text_upper.find('DEPOSITS')
                print(f"  Location: character {idx}")
                print(f"  Sample: {all_text[idx:idx+200]}")
            else:
                print("✗ No 'DEPOSITS' section found")
            
            # Check for withdrawals section
            if 'WITHDRAWAL' in text_upper:
                print("\n✓ Found 'WITHDRAWAL' section")
                idx = text_upper.find('WITHDRAWAL')
                print(f"  Location: character {idx}")
                print(f"  Sample: {all_text[idx:idx+200]}")
            else:
                print("\n✗ No 'WITHDRAWAL' section found")
            
            print("\n" + "="*80)
            print("SAMPLE TRANSACTION LINES")
            print("="*80)
            
            # Look for lines with dates and amounts
            import re
            lines = all_text.split('\n')
            transaction_lines = []
            
            for line in lines:
                # Has a date pattern and amount pattern
                if re.search(r'\d{1,2}/\d{1,2}', line) and re.search(r'\d+\.\d{2}', line):
                    if len(line) > 15 and len(line) < 200:
                        transaction_lines.append(line.strip())
            
            print(f"\nFound {len(transaction_lines)} potential transaction lines")
            print("\nShowing first 20 lines:")
            for i, line in enumerate(transaction_lines[:20]):
                print(f"{i+1:3}. {line}")
            
            print("\n" + "="*80)
            print("ANALYSIS COMPLETE")
            print("="*80)
            print("\nPlease copy the output above and share it.")
            print("Look especially at the 'SAMPLE TRANSACTION LINES' section.")
            
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 test_statement_parser.py <path_to_bofa_statement.pdf>")
        print("\nExample:")
        print("  python3 test_statement_parser.py ~/Downloads/BOA_Statement.pdf")
    else:
        test_statement(sys.argv[1])
