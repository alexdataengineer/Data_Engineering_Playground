# 🛠️ Utilities

Collection of utility scripts, helper functions, and common tools used across the Data Engineering Playground projects.

## 🚀 Features

### 📊 Utility Components
- **Excel Data Processing** - Excel file reading and processing utilities
- **Data Validation** - Data quality and validation tools
- **DBT Utilities** - Database and dbt-related helpers
- **Common Functions** - Reusable functions across projects

### 🎯 Resources
- **Data Processing** - File handling and data manipulation
- **Configuration Management** - Settings and environment management
- **Logging and Monitoring** - Debugging and tracking tools
- **Testing Utilities** - Test data and validation helpers

## 📁 Project Structure

```
utils/
├── read_excel_data.py              # Excel data reading utility
├── test_excel_structure.py         # Excel structure testing
├── dag_run_dbt.py                  # DBT execution utility
└── README.md                       # This file
```

## 🛠️ Installation

### 1. Prerequisites
- Python 3.8 or higher
- Required data processing libraries

### 2. Install Dependencies
```bash
pip install -r ../requirements.txt
```

### 3. Utility-Specific Dependencies
- `pandas` - Data manipulation
- `openpyxl` - Excel file handling
- `xlrd` - Legacy Excel support
- `pyyaml` - Configuration files
- `python-dotenv` - Environment variables
- `logging` - Built-in logging

## 🚀 How to Use

### 1. Excel Data Reading
```bash
python read_excel_data.py
```

**Features:**
- Read Excel files with various formats
- Handle different sheet structures
- Data validation and cleaning
- Export to different formats

### 2. Excel Structure Testing
```bash
python test_excel_structure.py
```

**Features:**
- Validate Excel file structure
- Check required columns
- Test data types and formats
- Generate structure reports

### 3. DBT Execution
```bash
python dag_run_dbt.py
```

**Features:**
- Execute dbt commands programmatically
- Monitor dbt runs
- Handle dbt errors and retries
- Generate execution reports

## 📊 Data Processing Utilities

### Excel File Handling
```python
import pandas as pd
import openpyxl

def read_excel_file(file_path, sheet_name=None, skip_rows=0):
    """
    Read Excel file with error handling and validation
    """
    try:
        if sheet_name:
            data = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=skip_rows)
        else:
            data = pd.read_excel(file_path, skiprows=skip_rows)
        
        return data
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

def validate_excel_structure(data, required_columns):
    """
    Validate Excel file structure
    """
    missing_columns = set(required_columns) - set(data.columns)
    
    if missing_columns:
        print(f"Missing columns: {missing_columns}")
        return False
    
    return True
```

### Data Validation
```python
def validate_data_types(data, expected_types):
    """
    Validate data types of columns
    """
    validation_results = {}
    
    for column, expected_type in expected_types.items():
        if column in data.columns:
            actual_type = str(data[column].dtype)
            validation_results[column] = actual_type == expected_type
    
    return validation_results

def check_missing_values(data, threshold=0.1):
    """
    Check for missing values in dataset
    """
    missing_percentages = (data.isnull().sum() / len(data)) * 100
    problematic_columns = missing_percentages[missing_percentages > threshold]
    
    return problematic_columns
```

## 🔧 Configuration Management

### Environment Variables
```python
import os
from dotenv import load_dotenv

def load_config():
    """
    Load configuration from environment variables
    """
    load_dotenv()
    
    config = {
        'database_url': os.getenv('DATABASE_URL'),
        'api_key': os.getenv('API_KEY'),
        'log_level': os.getenv('LOG_LEVEL', 'INFO'),
        'data_path': os.getenv('DATA_PATH', './data/')
    }
    
    return config
```

### YAML Configuration
```python
import yaml

def load_yaml_config(config_path):
    """
    Load configuration from YAML file
    """
    try:
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return None

def save_yaml_config(config, config_path):
    """
    Save configuration to YAML file
    """
    try:
        with open(config_path, 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False
```

## 📝 Logging Utilities

### Custom Logger
```python
import logging
import sys
from datetime import datetime

def setup_logger(name, log_level=logging.INFO, log_file=None):
    """
    Setup custom logger with file and console handlers
    """
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Create formatters
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (optional)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger

def log_function_call(func):
    """
    Decorator to log function calls
    """
    def wrapper(*args, **kwargs):
        logger = logging.getLogger(func.__module__)
        logger.info(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} completed successfully")
            return result
        except Exception as e:
            logger.error(f"{func.__name__} failed with error: {e}")
            raise
    
    return wrapper
```

## 🔄 Database Utilities

### DBT Integration
```python
import subprocess
import json

def run_dbt_command(command, project_dir=None):
    """
    Execute dbt command and return results
    """
    try:
        if project_dir:
            cmd = f"cd {project_dir} && dbt {command}"
        else:
            cmd = f"dbt {command}"
        
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        
        return {
            'success': result.returncode == 0,
            'stdout': result.stdout,
            'stderr': result.stderr,
            'return_code': result.returncode
        }
    except Exception as e:
        return {
            'success': False,
            'error': str(e)
        }

def dbt_run_models(models=None, project_dir=None):
    """
    Run specific dbt models
    """
    command = "run"
    if models:
        command += f" --models {models}"
    
    return run_dbt_command(command, project_dir)

def dbt_test_models(models=None, project_dir=None):
    """
    Test specific dbt models
    """
    command = "test"
    if models:
        command += f" --models {models}"
    
    return run_dbt_command(command, project_dir)
```

## 📊 Data Export Utilities

### Multiple Format Export
```python
def export_data(data, file_path, format_type='csv'):
    """
    Export data to various formats
    """
    try:
        if format_type.lower() == 'csv':
            data.to_csv(file_path, index=False)
        elif format_type.lower() == 'excel':
            data.to_excel(file_path, index=False)
        elif format_type.lower() == 'json':
            data.to_json(file_path, orient='records')
        elif format_type.lower() == 'parquet':
            data.to_parquet(file_path, index=False)
        else:
            raise ValueError(f"Unsupported format: {format_type}")
        
        print(f"Data exported successfully to {file_path}")
        return True
    except Exception as e:
        print(f"Error exporting data: {e}")
        return False
```

### Batch Export
```python
def batch_export_dataframes(dataframes, output_dir, format_type='csv'):
    """
    Export multiple dataframes to files
    """
    import os
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    results = {}
    
    for name, df in dataframes.items():
        file_path = os.path.join(output_dir, f"{name}.{format_type}")
        success = export_data(df, file_path, format_type)
        results[name] = success
    
    return results
```

## 🧪 Testing Utilities

### Test Data Generation
```python
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_test_data(rows=1000, columns=None):
    """
    Generate test data for development and testing
    """
    if columns is None:
        columns = ['id', 'name', 'value', 'date', 'category']
    
    data = {}
    
    for col in columns:
        if col == 'id':
            data[col] = range(1, rows + 1)
        elif col == 'name':
            data[col] = [f"Test_{i}" for i in range(rows)]
        elif col == 'value':
            data[col] = np.random.normal(100, 20, rows)
        elif col == 'date':
            start_date = datetime.now() - timedelta(days=365)
            data[col] = [start_date + timedelta(days=i) for i in range(rows)]
        elif col == 'category':
            categories = ['A', 'B', 'C', 'D']
            data[col] = np.random.choice(categories, rows)
    
    return pd.DataFrame(data)

def create_mock_excel_file(file_path, sheets=None):
    """
    Create mock Excel file for testing
    """
    if sheets is None:
        sheets = {'Sheet1': generate_test_data(100)}
    
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        for sheet_name, data in sheets.items():
            data.to_excel(writer, sheet_name=sheet_name, index=False)
    
    print(f"Mock Excel file created: {file_path}")
```

## 📈 Performance Utilities

### Memory Usage Monitoring
```python
import psutil
import os

def get_memory_usage():
    """
    Get current memory usage
    """
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    
    return {
        'rss': memory_info.rss / 1024 / 1024,  # MB
        'vms': memory_info.vms / 1024 / 1024,  # MB
        'percent': process.memory_percent()
    }

def monitor_memory_usage(func):
    """
    Decorator to monitor memory usage of functions
    """
    def wrapper(*args, **kwargs):
        memory_before = get_memory_usage()
        
        result = func(*args, **kwargs)
        
        memory_after = get_memory_usage()
        memory_diff = memory_after['rss'] - memory_before['rss']
        
        print(f"{func.__name__} memory usage: {memory_diff:.2f} MB")
        
        return result
    
    return wrapper
```

## 📈 Next Steps

- [ ] Additional file format support
- [ ] Advanced data validation rules
- [ ] Performance optimization tools
- [ ] Automated testing framework
- [ ] Configuration management system
- [ ] Monitoring and alerting utilities

## ⚠️ Considerations

### Error Handling
- **Robust Error Handling** - Handle all possible exceptions
- **Graceful Degradation** - Continue operation when possible
- **Detailed Logging** - Log all errors and warnings
- **User Feedback** - Provide clear error messages

### Performance
- **Memory Management** - Optimize memory usage
- **Processing Speed** - Efficient algorithms and data structures
- **Resource Cleanup** - Proper cleanup of resources
- **Caching** - Cache frequently used data

---

**Developed for efficient and reliable data engineering utilities** 