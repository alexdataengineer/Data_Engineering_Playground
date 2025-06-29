#!/usr/bin/env python3
"""
Cosgrove Pulse Analyzer
Script to analyze and process data from "The Cosgrove Pulse - NEXGEN.xlsx"
"""

import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys
import warnings
warnings.filterwarnings('ignore')

class CosgrovePulseAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None
        self.last_week_data = None
        self.previous_week_data = None

    def load_data(self):
        try:
            print("📊 Loading spreadsheet data...")
            self.df = pd.read_excel(self.file_path, header=2)
            print(f"✅ Data loaded successfully!")
            print(f"📋 Rows: {len(self.df)}")
            print(f"📋 Columns: {len(self.df.columns)}")
            print(f"📋 Main columns: {list(self.df.columns[:10])}")
            return True
        except Exception as e:
            print(f"❌ Error loading data: {str(e)}")
            return False

    def find_last_week_data(self):
        try:
            week_ending_col = None
            for col in self.df.columns:
                if 'week' in str(col).lower() and 'ending' in str(col).lower():
                    week_ending_col = col
                    break
            if week_ending_col is None:
                print("❌ 'Week Ending' column not found!")
                print(f"Available columns: {list(self.df.columns)}")
                return False
            print(f"📅 Date column found: {week_ending_col}")
            self.df = self.df.dropna(subset=[week_ending_col])
            if not pd.api.types.is_datetime64_any_dtype(self.df[week_ending_col]):
                self.df[week_ending_col] = pd.to_datetime(self.df[week_ending_col], errors='coerce')
            self.df = self.df.dropna(subset=[week_ending_col])
            self.df = self.df.sort_values(week_ending_col)
            self.last_week_data = self.df.iloc[-1]
            if len(self.df) > 1:
                self.previous_week_data = self.df.iloc[-2]
            print(f"📅 Last week: {self.last_week_data[week_ending_col].strftime('%Y-%m-%d')}")
            if self.previous_week_data is not None:
                print(f"📅 Previous week: {self.previous_week_data[week_ending_col].strftime('%Y-%m-%d')}")
            return True
        except Exception as e:
            print(f"❌ Error finding week data: {str(e)}")
            return False

    def calculate_metrics(self):
        try:
            print("\n🧮 Calculating metrics...")
            col_mapping = self._map_columns()
            last_week = self.last_week_data
            def get_value(col_key):
                col = col_mapping.get(col_key)
                if col is not None and col in last_week:
                    val = last_week[col]
                    if pd.isna(val):
                        return 0
                    return val
                return 0
            total_units = get_value('total_units')
            occupied_units = get_value('occupied_units')
            vacant_rented = get_value('vacant_rented')
            vacant_unrented = get_value('vacant_unrented')
            physical_occupancy = (occupied_units / total_units * 100) if total_units > 0 else 0
            pre_leased = ((occupied_units + vacant_rented) / total_units * 100) if total_units > 0 else 0
            monthly_rent = get_value('monthly_rent')
            net_monthly_income = get_value('net_monthly_income')
            delinquency = get_value('delinquency')
            economic_occupancy = (net_monthly_income / monthly_rent * 100) if monthly_rent > 0 else 0
            guest_cards = get_value('guest_cards')
            applicants = get_value('applicants')
            closing_ratio = (applicants / guest_cards * 100) if guest_cards > 0 else 0
            delinquency_change = 0
            if self.previous_week_data is not None:
                prev_delinquency = self.previous_week_data.get(col_mapping.get('delinquency'), 0)
                if pd.isna(prev_delinquency):
                    prev_delinquency = 0
                delinquency_change = delinquency - prev_delinquency
            capex = get_value('capex')
            checking_5026 = get_value('checking_5026')
            business_checking_2487 = get_value('business_checking_2487')
            results = {
                'week_ending': last_week.get(col_mapping.get('week_ending'), 'N/A'),
                'total_units': total_units,
                'occupied_units': occupied_units,
                'vacant_rented': vacant_rented,
                'vacant_unrented': vacant_unrented,
                'physical_occupancy': physical_occupancy,
                'pre_leased': pre_leased,
                'monthly_rent': monthly_rent,
                'net_monthly_income': net_monthly_income,
                'economic_occupancy': economic_occupancy,
                'delinquency': delinquency,
                'delinquency_change': delinquency_change,
                'guest_cards': guest_cards,
                'applicants': applicants,
                'closing_ratio': closing_ratio,
                'capex': capex,
                'checking_5026': checking_5026,
                'business_checking_2487': business_checking_2487
            }
            return results
        except Exception as e:
            print(f"❌ Error calculating metrics: {str(e)}")
            return None

    def _map_columns(self):
        columns = [str(col).lower() for col in self.df.columns]
        mapping = {}
        for col in columns:
            if 'week ending' in col:
                mapping['week_ending'] = self.df.columns[columns.index(col)]
            elif 'total' in col and 'unit' in col:
                mapping['total_units'] = self.df.columns[columns.index(col)]
            elif 'occupied' in col and 'unit' in col:
                mapping['occupied_units'] = self.df.columns[columns.index(col)]
            elif 'vacant' in col and 'rented' in col:
                mapping['vacant_rented'] = self.df.columns[columns.index(col)]
            elif 'vacant' in col and 'unrented' in col:
                mapping['vacant_unrented'] = self.df.columns[columns.index(col)]
            elif 'monthly rent' in col:
                mapping['monthly_rent'] = self.df.columns[columns.index(col)]
            elif 'net monthly income' in col:
                mapping['net_monthly_income'] = self.df.columns[columns.index(col)]
            elif 'delinq' in col:
                mapping['delinquency'] = self.df.columns[columns.index(col)]
            elif 'guest card' in col:
                mapping['guest_cards'] = self.df.columns[columns.index(col)]
            elif 'applicant' in col and 'conversion' not in col:
                mapping['applicants'] = self.df.columns[columns.index(col)]
            elif 'capex' in col:
                mapping['capex'] = self.df.columns[columns.index(col)]
            elif '5026' in col:
                mapping['checking_5026'] = self.df.columns[columns.index(col)]
            elif '2487' in col:
                mapping['business_checking_2487'] = self.df.columns[columns.index(col)]
        print(f"🗺️ Column mapping: {mapping}")
        return mapping

    def display_results(self, results):
        if not results:
            print("❌ No results to display")
            return
        print("\n" + "="*60)
        print("📊 COSGROVE PULSE - NEXGEN REPORT")
        print("="*60)
        print(f"\n📅 Week: {results['week_ending']}")
        print("\n🏠 OCCUPANCY")
        print("-" * 30)
        print(f"📦 Total Units: {results['total_units']}")
        print(f"✅ Occupied Units: {results['occupied_units']}")
        print(f"📋 Vacant-Rented: {results['vacant_rented']}")
        print(f"🏚️ Vacant-Unrented: {results['vacant_unrented']}")
        print(f"📊 Physical Occupancy: {results['physical_occupancy']:.1f}%")
        print(f"📈 Pre-Leased: {results['pre_leased']:.1f}%")
        print("\n💰 FINANCIAL")
        print("-" * 30)
        print(f"💵 Monthly Rent: ${results['monthly_rent']:,.2f}")
        print(f"💸 Net Monthly Income: ${results['net_monthly_income']:,.2f}")
        print(f"📊 Economic Occupancy: {results['economic_occupancy']:.1f}%")
        print(f"⚠️ Delinquency: ${results['delinquency']:,.2f}")
        if results['delinquency_change'] != 0:
            change_emoji = "📈" if results['delinquency_change'] > 0 else "📉"
            print(f"{change_emoji} Delinquency Change: ${results['delinquency_change']:+,.2f}")
        print("\n👥 LEASING")
        print("-" * 30)
        print(f"📝 Guest Cards: {results['guest_cards']}")
        print(f"📋 Applicants: {results['applicants']}")
        print(f"🎯 Closing Ratio: {results['closing_ratio']:.1f}%")
        print("\n🏦 ACCOUNT BALANCES")
        print("-" * 30)
        print(f"💼 CAPEX: ${results['capex']:,.2f}")
        print(f"🏦 Checking 5026: ${results['checking_5026']:,.2f}")
        print(f"💳 Business Checking 2487: ${results['business_checking_2487']:,.2f}")
        print("\n" + "="*60)

    def save_to_excel(self, results):
        try:
            results_df = pd.DataFrame([results])
            with pd.ExcelWriter(self.file_path, mode='a', engine='openpyxl', if_sheet_exists='replace') as writer:
                results_df.to_excel(writer, sheet_name='Análise_Automática', index=False)
            print("✅ Results saved to 'Análise_Automática' tab")
            return True
        except Exception as e:
            print(f"❌ Error saving to Excel: {str(e)}")
            return False

    def generate_charts(self, results):
        try:
            import matplotlib.pyplot as plt
            plt.style.use('default')
            fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
            fig.suptitle('Cosgrove Pulse - Dashboard de Métricas', fontsize=16, fontweight='bold')
            occupancy_data = [results['physical_occupancy'], results['pre_leased']]
            occupancy_labels = ['Ocupação Física', 'Pré-Aluguel']
            colors = ['#2E8B57', '#4169E1']
            ax1.pie(occupancy_data, labels=occupancy_labels, colors=colors, autopct='%1.1f%%', startangle=90)
            ax1.set_title('Taxas de Ocupação (%)')
            financial_metrics = ['Aluguel Mensal', 'Receita Líquida', 'Inadimplência']
            financial_values = [results['monthly_rent'], results['net_monthly_income'], results['delinquency']]
            bars = ax2.bar(financial_metrics, financial_values, color=['#32CD32', '#4169E1', '#DC143C'])
            ax2.set_title('Métricas Financeiras ($)')
            ax2.tick_params(axis='x', rotation=45)
            for bar, value in zip(bars, financial_values):
                ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(financial_values)*0.01,
                        f'${value:,.0f}', ha='center', va='bottom')
            leasing_data = [results['guest_cards'], results['applicants']]
            leasing_labels = ['Guest Cards', 'Applicants']
            ax3.bar(leasing_labels, leasing_data, color=['#FFD700', '#FF6347'])
            ax3.set_title('Atividade de Leasing')
            ax3.set_ylabel('Quantidade')
            for i, v in enumerate(leasing_data):
                ax3.text(i, v + max(leasing_data)*0.01, str(v), ha='center', va='bottom')
            bank_accounts = ['CAPEX', 'Checking 5026', 'Business 2487']
            bank_balances = [results['capex'], results['checking_5026'], results['business_checking_2487']]
            ax4.barh(bank_accounts, bank_balances, color=['#20B2AA', '#9370DB', '#FF8C00'])
            ax4.set_title('Saldos Bancários ($)')
            ax4.set_xlabel('Valor ($)')
            for i, v in enumerate(bank_balances):
                ax4.text(v + max(bank_balances)*0.01, i, f'${v:,.0f}', va='center')
            plt.tight_layout()
            chart_path = os.path.join(os.path.dirname(self.file_path), 'cosgrove_pulse_charts.png')
            plt.savefig(chart_path, dpi=300, bbox_inches='tight')
            plt.show()
            print(f"📊 Gráficos salvos em: {chart_path}")
            return True
        except ImportError:
            print("❌ matplotlib não está instalado. Instale com: pip install matplotlib")
            return False
        except Exception as e:
            print(f"❌ Error generating charts: {str(e)}")
            return False

def main():
    print("🚀 COSGROVE PULSE ANALYZER")
    print("=" * 40)
    file_path = "/Users/alexsandersilveira/Downloads/The Cosgrove Pulse- NEXGEN.xlsx"
    if not os.path.exists(file_path):
        print(f"❌ Arquivo não encontrado: {file_path}")
        return
    analyzer = CosgrovePulseAnalyzer(file_path)
    if not analyzer.load_data():
        return
    if not analyzer.find_last_week_data():
        return
    results = analyzer.calculate_metrics()
    if not results:
        return
    analyzer.display_results(results)
    while True:
        print("\n🤔 O que você gostaria de fazer?")
        print("1. 💾 Salvar análise em nova aba do Excel")
        print("2. 📊 Gerar gráficos")
        print("3. 🔄 Recalcular métricas")
        print("4. ❌ Sair")
        choice = input("\nEscolha uma opção (1-4): ").strip()
        if choice == '1':
            analyzer.save_to_excel(results)
        elif choice == '2':
            analyzer.generate_charts(results)
        elif choice == '3':
            results = analyzer.calculate_metrics()
            if results:
                analyzer.display_results(results)
        elif choice == '4':
            print("👋 Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main() 