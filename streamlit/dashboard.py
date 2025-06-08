import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Configuração da página
st.set_page_config(
    page_title="Dashboard de Demonstração",
    page_icon="📊",
    layout="wide"
)

# Título do dashboard
st.title("📊 Dashboard de Demonstração")
st.markdown("---")

# Criando dados fake de forma mais simples
def generate_fake_data():
    dates = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
    np.random.seed(42)
    
    data = {
        'Data': dates,
        'Vendas': np.random.normal(1000, 200, len(dates)),
        'Clientes': np.random.normal(50, 10, len(dates)),
        'Satisfação': np.random.uniform(3.5, 5, len(dates))
    }
    return pd.DataFrame(data)

# Gerando os dados
df = generate_fake_data()

# Sidebar com filtros
st.sidebar.header("Filtros")
data_inicio = st.sidebar.date_input(
    "Data Inicial",
    value=df['Data'].min(),
    min_value=df['Data'].min(),
    max_value=df['Data'].max()
)
data_fim = st.sidebar.date_input(
    "Data Final",
    value=df['Data'].max(),
    min_value=df['Data'].min(),
    max_value=df['Data'].max()
)

# Filtrando dados
df_filtrado = df[(df['Data'].dt.date >= data_inicio) & (df['Data'].dt.date <= data_fim)]

# Métricas principais
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(
        "Vendas Médias",
        f"R$ {df_filtrado['Vendas'].mean():,.2f}",
        f"{((df_filtrado['Vendas'].mean() / df['Vendas'].mean() - 1) * 100):,.1f}%"
    )
with col2:
    st.metric(
        "Clientes Médias",
        f"{df_filtrado['Clientes'].mean():,.0f}",
        f"{((df_filtrado['Clientes'].mean() / df['Clientes'].mean() - 1) * 100):,.1f}%"
    )
with col3:
    st.metric(
        "Satisfação Média",
        f"{df_filtrado['Satisfação'].mean():,.1f}",
        f"{((df_filtrado['Satisfação'].mean() / df['Satisfação'].mean() - 1) * 100):,.1f}%"
    )

# Gráficos
st.markdown("### 📈 Análise de Vendas")
fig_vendas = px.line(
    df_filtrado,
    x='Data',
    y='Vendas',
    title='Vendas ao Longo do Tempo'
)
st.plotly_chart(fig_vendas, use_container_width=True)

# Gráfico de barras para clientes
st.markdown("### 👥 Análise de Clientes")
fig_clientes = px.bar(
    df_filtrado,
    x='Data',
    y='Clientes',
    title='Número de Clientes por Dia'
)
st.plotly_chart(fig_clientes, use_container_width=True)

# Gráfico de satisfação
st.markdown("### 😊 Satisfação dos Clientes")
fig_satisfacao = px.scatter(
    df_filtrado,
    x='Data',
    y='Satisfação',
    title='Nível de Satisfação dos Clientes',
    color='Satisfação',
    color_continuous_scale='RdYlGn'
)
st.plotly_chart(fig_satisfacao, use_container_width=True)

# Tabela de dados
st.markdown("### 📋 Dados Detalhados")
st.dataframe(
    df_filtrado.style.format({
        'Vendas': 'R$ {:,.2f}',
        'Clientes': '{:,.0f}',
        'Satisfação': '{:,.1f}'
    }),
    use_container_width=True
)
