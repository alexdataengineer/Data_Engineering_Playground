# 🚀 Data Engineering Playground

This repository is a **personal workspace** for exploring, prototyping, and building data engineering solutions using **Python**, **PySpark**, **Airflow**, **dbt**, **Databricks**, and other modern technologies.

## 📁 Project Structure

### 🏗️ Infrastructure & Orchestration
- `dags/` - Apache Airflow DAGs for pipeline orchestration
- `docker-composer/` - Docker environments for local development
- `databricks/` - Databricks configurations and assets
- `dbt/` - dbt project with bronze/silver/gold models

### 📊 Data Analysis Projects
- `cosgrove/` - Complete system for Cosgrove Pulse spreadsheet analysis
- `finance/` - Financial data pipelines and analysis
- `tesla/` - Tesla-specific data analytics

### 🕷️ Web Scraping & Data Collection
- `scraping/` - Web scraping scripts for data collection
- `apis/` - Integrations with external APIs

### 📈 Dashboards & Visualization
- `dashboards/` - Streamlit dashboards and other visualizations
- `notebooks/` - Jupyter notebooks for EDA and prototyping

### 🧠 Machine Learning
- `ml/` - Machine learning scripts and models
- `analytics/` - Advanced analytics and modeling

### 🛠️ Utilities & Scripts
- `utils/` - Utility scripts and helpers
- `scripts/` - Automation and processing scripts

## 🧰 Tech Stack

### Core Technologies
- **Python 3.x** - Main programming language
- **Apache Spark (PySpark)** - Distributed processing
- **Apache Airflow** - Workflow orchestration
- **dbt (Data Build Tool)** - Data transformation
- **Databricks** - Analytics platform

### Frameworks & Libraries
- **Streamlit** - Interactive dashboards
- **Pandas/NumPy** - Data manipulation
- **Plotly/Matplotlib** - Visualizations
- **Requests/BeautifulSoup** - Web scraping
- **Docker** - Containerization

### Databases & Storage
- **SQL Server** - Main database
- **Azure Data Lake** - Data storage
- **Delta Lake** - Data format

## 🚀 Main Projects

### 📊 Cosgrove Pulse Analyzer
Complete system for analysis and visualization of "The Cosgrove Pulse - NEXGEN.xlsx" spreadsheet
- Automatic occupancy metrics analysis
- Interactive dashboard with Streamlit
- Real-time KPI calculations

### 🕷️ Web Scraping Suite
Collection of scripts for automated data collection
- Scrapers for clinics and companies
- Email and contact information collection
- Data processing and cleaning

### 💰 Finance Data Pipeline
Complete pipeline for financial data
- Financial API ingestion
- Processing with PySpark
- Automated analysis and reporting

### 🚗 Tesla Analytics
Tesla-specific data analytics
- EDA notebooks
- Predictive models
- Monitoring dashboards

## 🛠️ How to Use

### Initial Setup
```bash
# Clone the repository
git clone <repository-url>
cd Data_Engineering_Playground

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit the .env file with your settings
```

### Running Projects

#### Cosgrove Analyzer
```bash
python run_cosgrove_analyzer.py
# or
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

- [ ] Migration to organized project structure
- [ ] Complete documentation for each project
- [ ] Automated tests
- [ ] CI/CD pipeline
- [ ] Monitoring and alerts
- [ ] Performance optimization

## 🤝 Contributions

This is a personal project, but feel free to explore and use as a reference. If you find something useful or have suggestions, open an issue or get in touch.

## 📝 License

Personal project for educational and professional development purposes.

---

Developed by Alexsander Silveira

