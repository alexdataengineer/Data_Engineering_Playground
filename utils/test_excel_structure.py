#!/usr/bin/env python3
"""
Test script to understand the Excel structure
"""

import pandas as pd
import os

def test_excel_structure():
    file_path = "/Users/alexsandersilveira/Downloads/The Cosgrove Pulse- NEXGEN.xlsx"
    
    print("🔍 Testing Excel file structure...")
    print(f"📁 File path: {file_path}")
    print(f"📄 File exists: {os.path.exists(file_path)}")
    
    try:
        # Read all sheets
        excel_file = pd.ExcelFile(file_path)
        print(f"\n📋 Sheets found: {excel_file.sheet_names}")
        
        # Test reading with different header positions
        for header_row in [0, 1, 2, 3]:
            print(f"\n📊 Testing with header_row={header_row}:")
            try:
                df = pd.read_excel(file_path, header=header_row)
                print(f"   ✅ Success! Rows: {len(df)}, Columns: {len(df.columns)}")
                print(f"   📋 First 5 columns: {list(df.columns[:5])}")
                
                # Show first few rows
                print(f"   📄 First 3 rows:")
                print(df.head(3).to_string())
                
            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
        
        # Try to find Week Ending column
        print(f"\n🔍 Looking for 'Week Ending' column...")
        for header_row in [0, 1, 2, 3]:
            try:
                df = pd.read_excel(file_path, header=header_row)
                columns_lower = [str(col).lower() for col in df.columns]
                
                week_ending_found = False
                for i, col in enumerate(columns_lower):
                    if 'week' in col and 'ending' in col:
                        print(f"   ✅ Found 'Week Ending' at header_row={header_row}, column: {df.columns[i]}")
                        week_ending_found = True
                        break
                
                if not week_ending_found:
                    print(f"   ❌ No 'Week Ending' found at header_row={header_row}")
                    
            except Exception as e:
                print(f"   ❌ Error at header_row={header_row}: {str(e)}")
        
    except Exception as e:
        print(f"❌ Error reading Excel file: {str(e)}")

if __name__ == "__main__":
    test_excel_structure() 