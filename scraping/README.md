# 🕷️ Web Scraping Suite

Collection of scripts for automated data collection from websites, with focus on clinics and companies.

## 🚀 Features

### 📋 Available Scrapers
- **Simple Clinic Scraper** - Basic clinic information collection
- **Advanced Clinic Scraper** - Advanced collection with more details
- **Clinic Email Scraper** - Specific focus on contact emails
- **Test Scraper** - Test and validation script

### 🎯 Resources
- **Automated collection** of website data
- **Intelligent processing** of information
- **Export** to CSV and TXT
- **Flexible configuration** via configuration files
- **Robust error handling**

## 📁 Project Structure

```
scraping/
├── simple_clinic_scraper.py           # Basic scraper
├── simple_clinic_scraper_minimal.py   # Minimalist version
├── simple_clinic_scraper_no_pandas.py # Without pandas dependency
├── advanced_clinic_scraper.py         # Advanced scraper
├── clinic_email_scraper.py            # Email focus
├── test_scraper.py                    # Test script
├── run_scraper.py                     # Main executor
├── config.py                          # Configurations
├── example_urls.csv                   # Example URLs
├── clinicas_emails.csv                # Collected data
├── clinicas_emails.txt                # Data in text format
├── requirements.txt                   # Main dependencies
├── requirements_minimal.txt           # Minimal dependencies
├── requirements_python313.txt         # For Python 3.13
├── INSTALACAO_RAPIDA.md               # Quick guide
└── README.md                          # This file
```

## 🛠️ Installation

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 2. Install Dependencies

#### Option 1: Complete Dependencies
```bash
pip install -r requirements.txt
```

#### Option 2: Minimal Dependencies
```bash
pip install -r requirements_minimal.txt
```

#### Option 3: Python 3.13
```bash
pip install -r requirements_python313.txt
```

### 3. Main Dependencies
- `requests` - HTTP requests
- `beautifulsoup4` - HTML parsing
- `pandas` - Data manipulation
- `selenium` - Browser automation (optional)
- `lxml` - XML/HTML parser

## 🚀 How to Use

### Option 1: Main Executor
```bash
python run_scraper.py
```

### Option 2: Specific Scrapers

#### Simple Clinic Scraper
```bash
python simple_clinic_scraper.py
```

#### Advanced Clinic Scraper
```bash
python advanced_clinic_scraper.py
```

#### Clinic Email Scraper
```bash
python clinic_email_scraper.py
```

#### Test Scraper
```bash
python test_scraper.py
```

## ⚙️ Configuration

### Configuration File
Edit `config.py` to customize:

```python
# Scraping configurations
SCRAPING_CONFIG = {
    'timeout': 30,
    'retry_attempts': 3,
    'delay_between_requests': 2,
    'user_agent': 'Mozilla/5.0...'
}

# URLs for scraping
URLS = [
    'https://example1.com',
    'https://example2.com'
]
```

### Example URLs
Use `example_urls.csv` to add URLs:

```csv
url,name,category
https://clinic1.com,Clinic A,Medicine
https://clinic2.com,Clinic B,Dentist
```

## 📊 Collected Data

### CSV Format
```csv
name,email,phone,address,website
Clinic A,contact@clinica.com,(11) 9999-9999,Street A, 123,https://clinica.com
Clinic B,contact@clinicb.com,(11) 8888-8888,Street B, 456,https://clinicb.com
```

### TXT Format
```
Clinic A
Email: contact@clinica.com
Phone: (11) 9999-9999
Address: Street A, 123
Website: https://clinica.com

Clinic B
Email: contact@clinicb.com
Phone: (11) 8888-8888
Address: Street B, 456
Website: https://clinicb.com
```

## 🔧 Customization

### Add New Fields
Edit the desired scraper to collect new data:

```python
def extract_data(soup):
    data = {}
    data['name'] = soup.find('h1').text.strip()
    data['email'] = soup.find('a', href='mailto:').text.strip()
    data['phone'] = soup.find('span', class_='phone').text.strip()
    # Add new fields here
    return data
```

### New Site Types
Create a new scraper based on existing ones:

```python
class CustomScraper:
    def __init__(self, config):
        self.config = config
    
    def scrape(self, url):
        # Implement your scraping logic
        pass
```

## 🐛 Troubleshooting

### Error: "Connection timeout"
- Check your internet connection
- Increase timeout in configuration file
- Check if the site is accessible

### Error: "Element not found"
- The site may have changed its structure
- Check if CSS selectors are still valid
- Use test_scraper.py for debugging

### Error: "Rate limiting"
- Increase delay between requests
- Use proxies if necessary
- Implement User-Agent rotation

### Error: "Permission denied"
- Check if you have permission to write to directory
- Run with appropriate privileges

## 📈 Next Steps

- [ ] Integration with geolocation APIs
- [ ] Automatic email validation
- [ ] Dashboard for monitoring
- [ ] Scraping scheduling
- [ ] Database integration
- [ ] Machine learning for pattern detection

## ⚠️ Legal Considerations

- Respect the `robots.txt` of sites
- Don't overload servers
- Check terms of use of sites
- Use collected data ethically

---

**Developed for efficient and responsible web data collection** 