#!/usr/bin/env python3
"""
Cosgrove Pulse Dashboard
Interactive dashboard for Cosgrove Pulse - NEXGEN data
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'python scripts ML'))

try:
    from cosgrove_pulse_analyzer import CosgrovePulseAnalyzer # type: ignore
except ImportError:
    st.error("❌ Could not import analyzer. Check if cosgrove_pulse_analyzer.py is in the correct location.")
    st.stop()

def main():
    st.set_page_config(
        page_title="Cosgrove Pulse Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.title("📊 Cosgrove Pulse - NEXGEN Dashboard")
    st.markdown("---")
    with st.sidebar:
        st.header("⚙️ Settings")
        file_path = st.text_input(
            "📁 Excel file path",
            value="/Users/alexsandersilveira/Downloads/The Cosgrove Pulse- NEXGEN.xlsx",
            help="Full path to the Excel file"
        )
        if st.button("🔄 Load Data", type="primary"):
            st.session_state.load_data = True
        st.markdown("---")
        st.markdown("### 📈 Main Metrics")
        st.markdown("- **Physical Occupancy**: Occupied Units / Total Units")
        st.markdown("- **Pre-Leased**: (Occupied + Vacant-Rented) / Total Units")
        st.markdown("- **Economic Occupancy**: Net Monthly Income / Monthly Rent")
        st.markdown("- **Closing Ratio**: Applicants / Guest Cards")
    if 'load_data' not in st.session_state:
        st.session_state.load_data = False
    if st.session_state.load_data:
        analyzer = CosgrovePulseAnalyzer(file_path)
        with st.spinner("📊 Loading spreadsheet data..."):
            if not analyzer.load_data():
                st.error("❌ Error loading spreadsheet data!")
                return
            if not analyzer.find_last_week_data():
                st.error("❌ Error finding week data!")
                return
            results = analyzer.calculate_metrics()
            if not results:
                st.error("❌ Error calculating metrics!")
                return
        st.success("✅ Data loaded successfully!")
        st.session_state.analyzer = analyzer
        st.session_state.results = results
        st.session_state.load_data = False
    if 'results' in st.session_state and st.session_state.results:
        results = st.session_state.results
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric(
                label="🏠 Physical Occupancy",
                value=f"{results['physical_occupancy']:.1f}%",
                delta=f"{results['occupied_units']}/{results['total_units']} units"
            )
        with col2:
            st.metric(
                label="📈 Pre-Leased",
                value=f"{results['pre_leased']:.1f}%",
                delta=f"{results['occupied_units'] + results['vacant_rented']}/{results['total_units']} units"
            )
        with col3:
            st.metric(
                label="💰 Economic Occupancy",
                value=f"{results['economic_occupancy']:.1f}%",
                delta=f"${results['net_monthly_income']:,.0f} income"
            )
        with col4:
            st.metric(
                label="🎯 Closing Ratio",
                value=f"{results['closing_ratio']:.1f}%",
                delta=f"{results['applicants']}/{results['guest_cards']} ratio"
            )
        st.markdown("---")
        tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🏠 Occupancy", "💰 Financial", "👥 Leasing"])
        with tab1:
            st.subheader("📊 Metrics Overview")
            col1, col2 = st.columns(2)
            with col1:
                occupancy_data = {
                    'Occupied': results['occupied_units'],
                    'Vacant-Rented': results['vacant_rented'],
                    'Vacant-Unrented': results['vacant_unrented']
                }
                fig_pie = px.pie(
                    values=list(occupancy_data.values()),
                    names=list(occupancy_data.keys()),
                    title="Unit Distribution",
                    color_discrete_sequence=['#2E8B57', '#4169E1', '#DC143C']
                )
                fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig_pie, use_container_width=True)
            with col2:
                financial_data = {
                    'Metric': ['Monthly Rent', 'Net Monthly Income', 'Delinquency'],
                    'Value ($)': [results['monthly_rent'], results['net_monthly_income'], results['delinquency']]
                }
                df_financial = pd.DataFrame(financial_data)
                fig_bar = px.bar(
                    df_financial,
                    x='Metric',
                    y='Value ($)',
                    title="Financial Metrics",
                    color='Metric',
                    color_discrete_sequence=['#32CD32', '#4169E1', '#DC143C']
                )
                fig_bar.update_layout(showlegend=False)
                st.plotly_chart(fig_bar, use_container_width=True)
        with tab2:
            st.subheader("🏠 Occupancy Analysis")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 📋 Occupancy Details")
                occupancy_metrics = {
                    "Total Units": results['total_units'],
                    "Occupied Units": results['occupied_units'],
                    "Vacant-Rented": results['vacant_rented'],
                    "Vacant-Unrented": results['vacant_unrented']
                }
                for metric, value in occupancy_metrics.items():
                    st.metric(metric, value)
            with col2:
                occupancy_data = {
                    'Type': ['Occupied', 'Vacant-Rented', 'Vacant-Unrented'],
                    'Count': [results['occupied_units'], results['vacant_rented'], results['vacant_unrented']]
                }
                df_occupancy = pd.DataFrame(occupancy_data)
                fig_hbar = px.bar(
                    df_occupancy,
                    x='Count',
                    y='Type',
                    orientation='h',
                    title="Unit Distribution",
                    color='Type',
                    color_discrete_sequence=['#2E8B57', '#4169E1', '#DC143C']
                )
                fig_hbar.update_layout(showlegend=False)
                st.plotly_chart(fig_hbar, use_container_width=True)
        with tab3:
            st.subheader("💰 Financial Analysis")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 💵 Financial Metrics")
                financial_metrics = {
                    "Monthly Rent": f"${results['monthly_rent']:,.2f}",
                    "Net Monthly Income": f"${results['net_monthly_income']:,.2f}",
                    "Delinquency": f"${results['delinquency']:,.2f}",
                    "Economic Occupancy": f"{results['economic_occupancy']:.1f}%"
                }
                for metric, value in financial_metrics.items():
                    st.metric(metric, value)
                if results['delinquency_change'] != 0:
                    change_emoji = "📈" if results['delinquency_change'] > 0 else "📉"
                    st.metric(
                        "Delinquency Change",
                        f"${results['delinquency_change']:+,.2f}",
                        delta=f"{change_emoji} {results['delinquency_change']:+,.2f}"
                    )
            with col2:
                bank_data = {
                    'Account': ['CAPEX', 'Checking 5026', 'Business 2487'],
                    'Balance ($)': [results['capex'], results['checking_5026'], results['business_checking_2487']]
                }
                df_bank = pd.DataFrame(bank_data)
                fig_bank = px.bar(
                    df_bank,
                    x='Account',
                    y='Balance ($)',
                    title="Account Balances",
                    color='Account',
                    color_discrete_sequence=['#20B2AA', '#9370DB', '#FF8C00']
                )
                fig_bank.update_layout(showlegend=False)
                st.plotly_chart(fig_bank, use_container_width=True)
        with tab4:
            st.subheader("👥 Leasing Analysis")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 📝 Leasing Metrics")
                leasing_metrics = {
                    "Guest Cards": results['guest_cards'],
                    "Applicants": results['applicants'],
                    "Closing Ratio": f"{results['closing_ratio']:.1f}%"
                }
                for metric, value in leasing_metrics.items():
                    st.metric(metric, value)
            with col2:
                leasing_data = {
                    'Metric': ['Guest Cards', 'Applicants'],
                    'Count': [results['guest_cards'], results['applicants']]
                }
                df_leasing = pd.DataFrame(leasing_data)
                fig_leasing = px.bar(
                    df_leasing,
                    x='Metric',
                    y='Count',
                    title="Leasing Activity",
                    color='Metric',
                    color_discrete_sequence=['#FFD700', '#FF6347']
                )
                fig_leasing.update_layout(showlegend=False)
                st.plotly_chart(fig_leasing, use_container_width=True)
        st.markdown("---")
        st.subheader("💾 Export Data")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Export to Excel"):
                if 'analyzer' in st.session_state:
                    if st.session_state.analyzer.save_to_excel(results):
                        st.success("✅ Data exported successfully!")
                    else:
                        st.error("❌ Error exporting data!")
        with col2:
            df_results = pd.DataFrame([results])
            csv = df_results.to_csv(index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name=f"cosgrove_pulse_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv"
            )
    else:
        st.info("👆 Use the sidebar to load spreadsheet data.")
        st.markdown("### 📋 How to use:")
        st.markdown("1. **Set the Excel file path** in the sidebar")
        st.markdown("2. **Click 'Load Data'** to process the spreadsheet")
        st.markdown("3. **Explore the tabs** for different views")
        st.markdown("4. **Export data** as needed")
        st.markdown("### 🎯 Features:")
        st.markdown("- 📊 **Automatic analysis** of occupancy metrics")
        st.markdown("- 💰 **Financial calculations** and changes")
        st.markdown("- 👥 **Leasing and conversion metrics**")
        st.markdown("- 📈 **Interactive charts** with Plotly")
        st.markdown("- 💾 **Export to Excel and CSV**")

if __name__ == "__main__":
    main() 