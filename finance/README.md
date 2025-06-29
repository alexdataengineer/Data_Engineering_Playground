# 💰 Finance Data Pipeline

Complete pipeline for ingestion, processing and analysis of financial data using PySpark, APIs and Jupyter notebooks.

## 🚀 Features

### 📊 Available Pipelines
- **Finance API Ingestion** - Ingestion of financial API data
- **Partitioned Bank Data Pipeline** - Processing of partitioned banking data
- **DAG Extract API Finance** - Orchestration with Airflow

### 🎯 Resources
- **Automated ingestion** of financial APIs
- **Distributed processing** with PySpark
- **Intelligent partitioning** of data
- **Orchestration** with Apache Airflow
- **Advanced analytics** with Jupyter notebooks

## 📁 Project Structure

```
finance/
├── Finance_API_ingestion.ipynb        # API ingestion notebook
├── PartitionedBankDataPipeline.ipynb  # Banking data pipeline
├── DAG_extract_API_Finance            # Airflow DAG
└── README.md                          # This file
```

## 🛠️ Installation

### 1. Prerequisites
- Python 3.8 or higher
- Apache Spark (PySpark)
- Apache Airflow
- Jupyter Notebook

### 2. Install Dependencies
```bash
pip install -r ../requirements.txt
```

### 3. Specific Dependencies
- `pyspark` - Distributed processing
- `requests` - HTTP requests for APIs
- `pandas` - Data manipulation
- `numpy` - Numerical calculations
- `matplotlib` - Visualizations
- `seaborn` - Statistical visualizations

## 🚀 How to Use

### 1. Finance API Ingestion
```bash
jupyter notebook Finance_API_ingestion.ipynb
```

**Features:**
- Connects to financial APIs
- Extracts real-time data
- Processes and cleans data
- Saves in structured format

### 2. Partitioned Bank Data Pipeline
```bash
jupyter notebook PartitionedBankDataPipeline.ipynb
```

**Features:**
- Processes banking data in batches
- Partitions data by date/region
- Optimizes query performance
- Generates automated reports

### 3. Airflow DAG
```bash
# The DAG will run automatically via Airflow
# Check status in Airflow UI
```

## 📊 Supported APIs

### Financial APIs
- **Alpha Vantage** - Market data
- **Yahoo Finance** - Stock prices
- **Quandl** - Economic data
- **FRED** - Federal Reserve data

### API Configuration
```python
# Configuration example
API_CONFIG = {
    'alpha_vantage': {
        'api_key': 'YOUR_API_KEY',
        'base_url': 'https://www.alphavantage.co/query'
    },
    'yahoo_finance': {
        'base_url': 'https://query1.finance.yahoo.com'
    }
}
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```bash
# APIs
ALPHA_VANTAGE_API_KEY=your_key_here
YAHOO_FINANCE_API_KEY=your_key_here

# Database
DB_HOST=localhost
DB_PORT=5432
DB_NAME=finance_data
DB_USER=username
DB_PASSWORD=password

# Spark
SPARK_MASTER=local[*]
SPARK_DRIVER_MEMORY=2g
```

### Spark Configuration
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("FinanceDataPipeline") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()
```

## 📈 Data Structure

### Market Data
```python
# Example schema
market_data_schema = StructType([
    StructField("symbol", StringType(), False),
    StructField("date", DateType(), False),
    StructField("open", DoubleType(), True),
    StructField("high", DoubleType(), True),
    StructField("low", DoubleType(), True),
    StructField("close", DoubleType(), True),
    StructField("volume", LongType(), True)
])
```

### Banking Data
```python
# Example schema
bank_data_schema = StructType([
    StructField("account_id", StringType(), False),
    StructField("transaction_date", TimestampType(), False),
    StructField("amount", DecimalType(10,2), True),
    StructField("category", StringType(), True),
    StructField("description", StringType(), True)
])
```

## 🔄 Processing Pipeline

### 1. Ingestion (Bronze)
```python
# Extract data from APIs
raw_data = extract_from_api(api_config)

# Save raw data
raw_data.write.mode("append").parquet("bronze/market_data")
```

### 2. Processing (Silver)
```python
# Clean and validate data
cleaned_data = clean_and_validate(raw_data)

# Transform data
transformed_data = transform_data(cleaned_data)

# Save processed data
transformed_data.write.mode("overwrite").parquet("silver/market_data")
```

### 3. Analysis (Gold)
```python
# Calculate metrics
metrics = calculate_metrics(transformed_data)

# Generate reports
reports = generate_reports(metrics)

# Save final data
reports.write.mode("overwrite").parquet("gold/reports")
```

## 📊 Available Analyses

### Market Metrics
- **Daily return** = (Close - Open) / Open
- **Volatility** = Standard deviation of returns
- **Average volume** = Moving average of volume
- **Correlation** between assets

### Technical Indicators
- **Moving Average** (SMA, EMA)
- **RSI** (Relative Strength Index)
- **MACD** (Moving Average Convergence Divergence)
- **Bollinger Bands**

### Banking Analysis
- **Cash flow** by period
- **Transaction categorization**
- **Spending analysis** by category
- **Projections** based on history

## 🚀 Optimizations

### Partitioning
```python
# Partition by date for better performance
data.write.partitionBy("date").parquet("partitioned_data")
```

### Cache
```python
# Cache frequently accessed data
frequently_used_data.cache()
```

### Broadcast Variables
```python
# Broadcast small datasets
small_lookup_table = spark.sparkContext.broadcast(lookup_data)
```

## 📈 Monitoring

### Performance Metrics
- **Execution time** of pipelines
- **Data volume** processed
- **Error rate** in APIs
- **Resource usage** of Spark

### Alerts
- **Failures** in API ingestion
- **Timeouts** in processing
- **Anomalies** in data
- **API quota** exceeded

## 🐛 Troubleshooting

### Error: "API rate limit exceeded"
- Implement delays between requests
- Use multiple API keys
- Implement retry logic

### Error: "Out of memory"
- Increase driver memory
- Use adequate partitioning
- Implement strategic cache

### Error: "Connection timeout"
- Increase timeouts
- Implement circuit breaker
- Use connection pooling

## 📈 Next Steps

- [ ] Integration with more financial APIs
- [ ] Machine learning for predictions
- [ ] Real-time dashboard
- [ ] Automatic alerts
- [ ] Strategy backtesting
- [ ] Trading system integration

## ⚠️ Considerations

### Security
- **API Keys** must be protected
- **Sensitive data** must be encrypted
- **Access** must be controlled

### Compliance
- **Financial regulations**
- **Data auditing**
- **Data retention**

---

**Developed for professional financial data analysis** 