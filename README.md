# 🚀 Data Engineering Playground

Este repositório é um **workspace pessoal** para explorar, prototipar e construir soluções de engenharia de dados usando **Python**, **PySpark**, **Airflow**, **dbt**, **Databricks** e outras tecnologias modernas.

## 📁 Estrutura Organizada por Projetos

### 🏗️ **Infraestrutura & Orquestração**
- `dags/` - Apache Airflow DAGs para orquestração de pipelines
- `docker-composer/` - Ambientes Docker para desenvolvimento local
- `databricks/` - Configurações e assets do Databricks
- `dbt/` - Projeto dbt com modelos bronze/silver/gold

### 📊 **Projetos de Análise de Dados**
- `cosgrove/` - Sistema completo de análise da planilha Cosgrove Pulse
- `finance/` - Pipelines e análises de dados financeiros
- `tesla/` - Análises específicas sobre dados da Tesla

### 🕷️ **Web Scraping & Coleta**
- `scraping/` - Scripts de web scraping para coleta de dados
- `apis/` - Integrações com APIs externas

### 📈 **Dashboards & Visualização**
- `dashboards/` - Dashboards Streamlit e outras visualizações
- `notebooks/` - Jupyter notebooks para EDA e prototipagem

### 🧠 **Machine Learning**
- `ml/` - Scripts e modelos de machine learning
- `analytics/` - Análises avançadas e modelagem

### 🛠️ **Utilitários & Scripts**
- `utils/` - Scripts utilitários e helpers
- `scripts/` - Scripts de automação e processamento

## 🧰 Stack Tecnológico

### **Core Technologies**
- **Python 3.x** - Linguagem principal
- **Apache Spark (PySpark)** - Processamento distribuído
- **Apache Airflow** - Orquestração de workflows
- **dbt (Data Build Tool)** - Transformação de dados
- **Databricks** - Plataforma de analytics

### **Frameworks & Libraries**
- **Streamlit** - Dashboards interativos
- **Pandas/NumPy** - Manipulação de dados
- **Plotly/Matplotlib** - Visualizações
- **Requests/BeautifulSoup** - Web scraping
- **Docker** - Containerização

### **Databases & Storage**
- **SQL Server** - Banco de dados principal
- **Azure Data Lake** - Armazenamento de dados
- **Delta Lake** - Formato de dados

## 🚀 Projetos Principais

### 📊 **Cosgrove Pulse Analyzer**
Sistema completo para análise e visualização de dados da planilha "The Cosgrove Pulse - NEXGEN.xlsx"
- Análise automática de métricas de ocupação
- Dashboard interativo com Streamlit
- Cálculos de KPIs em tempo real

### 🕷️ **Web Scraping Suite**
Coleção de scripts para coleta automatizada de dados
- Scrapers para clínicas e empresas
- Coleta de emails e informações de contato
- Processamento e limpeza de dados

### 💰 **Finance Data Pipeline**
Pipeline completo para dados financeiros
- Ingestão de APIs financeiras
- Processamento com PySpark
- Análises e relatórios automatizados

### 🚗 **Tesla Analytics**
Análises específicas sobre dados da Tesla
- Notebooks de EDA
- Modelos preditivos
- Dashboards de monitoramento

## 🛠️ Como Usar

### **Setup Inicial**
```bash
# Clone o repositório
git clone <repository-url>
cd Data_Engineering_Playground

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

### **Executar Projetos**

#### Cosgrove Analyzer
```bash
python run_cosgrove_analyzer.py
# ou
streamlit run dashboards/cosgrove_dashboard.py
```

#### Web Scraping
```bash
cd scraping/
python run_scraper.py
```

#### Airflow DAGs
```bash
cd dags/
python kafka_stream.py
```

## 📋 Roadmap

- [ ] Migração para estrutura organizada por projetos
- [ ] Documentação completa de cada projeto
- [ ] Testes automatizados
- [ ] CI/CD pipeline
- [ ] Monitoramento e alertas
- [ ] Otimização de performance

## 🤝 Contribuições

Este é um projeto pessoal, mas sinta-se à vontade para explorar e usar como referência. Se encontrar algo útil ou tiver sugestões, abra uma issue ou entre em contato.

## 📝 Licença

Projeto pessoal para fins educacionais e de desenvolvimento profissional.

---

**Desenvolvido com ❤️ para explorar o mundo da Engenharia de Dados**

