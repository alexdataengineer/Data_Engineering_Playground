# 📊 Cosgrove Pulse Analyzer

Sistema completo para análise e visualização de dados da planilha "The Cosgrove Pulse - NEXGEN.xlsx".

## 🚀 Funcionalidades

### 📋 Análise Automática
- **Leitura inteligente** da planilha Excel (pula as 2 primeiras linhas)
- **Identificação automática** da última semana preenchida
- **Cálculos automáticos** de todas as métricas principais

### 🧮 Métricas Calculadas
- **Ocupação Física** = (Unidades Ocupadas ÷ Total) × 100%
- **Pré-Aluguel** = (Ocupadas + Vagas Alugadas ÷ Total) × 100%
- **Ocupação Econômica** = (Receita Líquida ÷ Aluguel Mensal) × 100%
- **Taxa de Fechamento** = (Applicants ÷ Guest Cards) × 100%
- **Variação de Inadimplência** (comparação com semana anterior)

### 📊 Visualizações
- **Dashboard interativo** com Streamlit
- **Gráficos dinâmicos** com Plotly
- **Métricas em tempo real** com formatação amigável
- **Exportação** para Excel e CSV

## 📁 Estrutura do Projeto

```
├── python scripts ML/
│   └── cosgrove_pulse_analyzer.py    # Analisador principal
├── streamlit/
│   └── cosgrove_dashboard.py         # Dashboard interativo
├── run_cosgrove_analyzer.py          # Script de execução
├── requirements.txt                  # Dependências
└── COSGROVE_README.md               # Este arquivo
```

## 🛠️ Instalação

### 1. Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### 2. Instalar Dependências
```bash
# Opção 1: Usar o script de execução
python run_cosgrove_analyzer.py
# Escolha opção 1 para instalar dependências

# Opção 2: Instalar manualmente
pip install -r requirements.txt
```

### 3. Dependências Instaladas
- `pandas` - Manipulação de dados
- `numpy` - Cálculos numéricos
- `openpyxl` - Leitura de arquivos Excel
- `matplotlib` - Geração de gráficos
- `streamlit` - Dashboard interativo
- `plotly` - Gráficos dinâmicos

## 🚀 Como Usar

### Opção 1: Script de Execução (Recomendado)
```bash
python run_cosgrove_analyzer.py
```

### Opção 2: Execução Direta

#### Analisador via Linha de Comando
```bash
python "python scripts ML/cosgrove_pulse_analyzer.py"
```

#### Dashboard Streamlit
```bash
streamlit run streamlit/cosgrove_dashboard.py
```

## 📊 Como Funciona

### 1. Leitura da Planilha
- Pula automaticamente as 2 primeiras linhas (títulos de seção)
- Usa a linha 3 como cabeçalho real
- Identifica automaticamente a coluna "Week Ending"

### 2. Mapeamento de Colunas
O sistema mapeia automaticamente as colunas baseado nos nomes:

#### 🏠 Ocupação
- `Total Units` → Total de unidades
- `Occupied Units` → Unidades ocupadas
- `Vacant-Rented` → Vagas já alugadas
- `Vacant-Unrented` → Vagas disponíveis

#### 💰 Financeiro
- `Monthly Rent` → Aluguel mensal
- `Net Monthly Income` → Receita líquida
- `Delinquency` → Inadimplência

#### 👥 Leasing
- `Guest Cards` → Cartões de visitantes
- `Applicants` → Candidatos

#### 🏦 Bancário
- `CAPEX` → Conta CAPEX
- `Checking 5026` → Conta operacional
- `Business Checking 2487` → Conta principal

### 3. Cálculos Automáticos
```python
# Ocupação Física
physical_occupancy = (occupied_units / total_units) * 100

# Pré-Aluguel
pre_leased = ((occupied_units + vacant_rented) / total_units) * 100

# Ocupação Econômica
economic_occupancy = (net_monthly_income / monthly_rent) * 100

# Taxa de Fechamento
closing_ratio = (applicants / guest_cards) * 100

# Variação de Inadimplência
delinquency_change = current_delinquency - previous_delinquency
```

## 📈 Dashboard Features

### 🎯 Métricas Principais
- Cards com métricas em tempo real
- Indicadores de variação (deltas)
- Formatação com emojis e cores

### 📊 Visualizações
- **Gráfico de Pizza**: Distribuição de unidades
- **Gráfico de Barras**: Métricas financeiras
- **Gráfico Horizontal**: Análise de ocupação
- **Gráfico de Saldos**: Contas bancárias

### 💾 Exportação
- **Excel**: Salva em nova aba da planilha original
- **CSV**: Download direto dos dados processados

## 🔧 Configuração

### Caminho do Arquivo
Por padrão, o sistema procura o arquivo em:
```
/Users/alexsandersilveira/Downloads/The Cosgrove Pulse- NEXGEN.xlsx
```

Para alterar, edite o arquivo `cosgrove_pulse_analyzer.py` na linha:
```python
file_path = "/Users/alexsandersilveira/Downloads/The Cosgrove Pulse- NEXGEN.xlsx"
```

### Total de Unidades
O sistema assume 36 unidades por padrão. Para alterar, edite a linha:
```python
total_units = last_week.get(col_mapping.get('total_units'), 36)  # Default 36
```

## 🐛 Solução de Problemas

### Erro: "Arquivo não encontrado"
- Verifique se o caminho do arquivo está correto
- Certifique-se de que o arquivo existe no local especificado

### Erro: "Coluna 'Week Ending' não encontrada"
- Verifique se a planilha tem a coluna "Week Ending"
- O sistema procura por variações como "Week Ending", "week ending", etc.

### Erro: "Erro ao carregar dados"
- Verifique se o arquivo não está aberto no Excel
- Certifique-se de que o arquivo não está corrompido

### Erro: "matplotlib não está instalado"
```bash
pip install matplotlib
```

## 📝 Exemplo de Saída

```
🚀 COSGROVE PULSE ANALYZER
========================================
📊 Carregando dados da planilha...
✅ Dados carregados com sucesso!
📋 Total de linhas: 52
📋 Total de colunas: 25
📅 Última semana: 15/12/2024

============================================================
📊 RELATÓRIO COSGROVE PULSE - NEXGEN
============================================================

📅 Semana: 2024-12-15

🏠 OCUPAÇÃO
------------------------------
📦 Total de Unidades: 36
✅ Unidades Ocupadas: 32
📋 Vagas Alugadas: 2
🏚️ Vagas Disponíveis: 2
📊 Ocupação Física: 88.9%
📈 Pré-Aluguel: 94.4%

💰 FINANCEIRO
------------------------------
💵 Aluguel Mensal: $45,000.00
💸 Receita Líquida: $42,500.00
📊 Ocupação Econômica: 94.4%
⚠️ Inadimplência: $2,500.00
📉 Variação Inadimplência: -$500.00

👥 LEASING
------------------------------
📝 Guest Cards: 15
📋 Applicants: 8
🎯 Taxa de Fechamento: 53.3%

🏦 SALDOS BANCÁRIOS
------------------------------
💼 CAPEX: $15,000.00
🏦 Checking 5026: $8,500.00
💳 Business Checking 2487: $25,000.00
============================================================
```

## 🤝 Contribuição

Para contribuir com melhorias:

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Implemente as melhorias
4. Teste com sua planilha
5. Envie um pull request

## 📞 Suporte

Para dúvidas ou problemas:
- Verifique a seção "Solução de Problemas"
- Teste com uma planilha de exemplo
- Verifique se todas as dependências estão instaladas

## 📄 Licença

Este projeto é de uso livre para análise de dados do Cosgrove Pulse. 