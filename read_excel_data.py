#!/usr/bin/env python3
"""
Simple script to read and display Excel data
"""

import pandas as pd
import os

def read_excel_data():
    file_path = "/Users/alexsandersilveira/Downloads/The Cosgrove Pulse- NEXGEN.xlsx"
    
    print("📊 Reading Excel file...")
    print(f"📁 File: {file_path}")
    
    try:
        # Read with header=2 (third row as header)
        df = pd.read_excel(file_path, header=2)
        
        print(f"✅ Successfully loaded!")
        print(f"📋 Total rows: {len(df)}")
        print(f"📋 Total columns: {len(df.columns)}")
        
        # Show all column names
        print(f"\n📋 All columns:")
        for i, col in enumerate(df.columns):
            print(f"  {i+1:2d}. {col}")
        
        # Remove rows with NaN Week Ending
        df_clean = df.dropna(subset=['Week Ending'])
        print(f"\n📋 Rows with valid dates: {len(df_clean)}")
        
        # Get the last row with valid data
        last_row = df_clean.iloc[-1]
        
        print(f"\n📅 Last week data (Week Ending): {last_row['Week Ending']}")
        print("\n" + "="*60)
        print("📊 KEY METRICS FROM SPREADSHEET")
        print("="*60)
        
        # Occupancy metrics
        print(f"\n🏠 OCCUPANCY:")
        print(f"  Total Units: {last_row['Total Units']}")
        print(f"  Occupied Units: {last_row['Occupied Units']}")
        print(f"  Vacant-Rented: {last_row['Vacant-Rented']}")
        print(f"  Vacant-Unrented: {last_row['Vacant-Unrented']}")
        print(f"  Physical Occupancy: {last_row['Physical Occupancy']:.1%}")
        print(f"  Pre-Leased: {last_row['Pre - Leased']:.1%}")
        
        # Financial metrics
        print(f"\n💰 FINANCIAL:")
        print(f"  Monthly Rent: ${last_row['Monthly Rent']:,.2f}")
        print(f"  Net Monthly Income: ${last_row['Net monthly income']:,.2f}")
        print(f"  Economic Occupancy: {last_row['Economic Occupancy']:.1%}")
        print(f"  Delinquency: ${last_row['Delinquency']:,.2f}")
        
        # Leasing metrics
        print(f"\n👥 LEASING:")
        print(f"  Guest Cards: {last_row['Guest Cards']}")
        print(f"  Applicants: {last_row['Applicants']}")
        print(f"  Closing Ratio: {last_row['Closing Ratio']:.1%}")
        
        # Account balances
        print(f"\n🏦 ACCOUNT BALANCES:")
        print(f"  CAPEX: ${last_row['CAPEX']:,.2f}")
        print(f"  Checking 5026: ${last_row['Checking 5026']:,.2f}")
        print(f"  Business Checking 2487: ${last_row['Business Ckg 2487']:,.2f}")
        
        # Show previous week for comparison
        if len(df_clean) > 1:
            prev_row = df_clean.iloc[-2]
            print(f"\n📈 COMPARISON WITH PREVIOUS WEEK:")
            print(f"  Previous Week: {prev_row['Week Ending']}")
            
            # Delinquency change
            delinquency_change = last_row['Delinquency'] - prev_row['Delinquency']
            print(f"  Delinquency Change: ${delinquency_change:+,.2f}")
            
            # Occupancy change
            occupancy_change = last_row['Physical Occupancy'] - prev_row['Physical Occupancy']
            print(f"  Physical Occupancy Change: {occupancy_change:+.1%}")
        
        print("\n" + "="*60)
        
        # Show last 5 rows for context
        print(f"\n📋 Last 5 weeks of data:")
        print(df_clean[['Week Ending', 'Total Units', 'Occupied Units', 'Physical Occupancy', 'Monthly Rent', 'Net monthly income']].tail())
        
    except Exception as e:
        print(f"❌ Error reading file: {str(e)}")

if __name__ == "__main__":
    read_excel_data() 