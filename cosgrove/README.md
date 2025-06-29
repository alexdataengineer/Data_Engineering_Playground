# 📊 Cosgrove Pulse Analyzer

Complete system for analysis and visualization of data from "The Cosgrove Pulse - NEXGEN.xlsx" spreadsheet.

## 🚀 Features

### 📋 Automatic Analysis
- **Intelligent reading** of Excel spreadsheet (skips first 2 rows)
- **Automatic identification** of the last filled week
- **Automatic calculations** of all main metrics

### 🧮 Calculated Metrics
- **Physical Occupancy** = (Occupied Units ÷ Total) × 100%
- **Pre-Leasing** = (Occupied + Rented Vacancies ÷ Total) × 100%
- **Economic Occupancy** = (Net Revenue ÷ Monthly Rent) × 100%
- **Closing Ratio** = (Applicants ÷ Guest Cards) × 100%
- **Delinquency Variation** (comparison with previous week)

### 📊 Visualizations
- **Interactive dashboard** with Streamlit
- **Dynamic charts** with Plotly
- **Real-time metrics** with friendly formatting
- **Export** to Excel and CSV

## 📁 Project Structure

```
cosgrove/
├── cosgrove_pulse_analyzer.py    # Main analyzer
├── run_cosgrove_analyzer.py      # Execution script
└── README.md                     # This file
```

## 🛠️ Installation

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 2. Install Dependencies
```bash
# Option 1: Use execution script
python run_cosgrove_analyzer.py
# Choose option 1 to install dependencies

# Option 2: Install manually
pip install -r ../requirements.txt
```

### 3. Installed Dependencies
- `pandas` - Data manipulation
- `numpy` - Numerical calculations
- `openpyxl` - Excel file reading
- `matplotlib` - Chart generation
- `streamlit` - Interactive dashboard
- `plotly` - Dynamic charts

## 🚀 How to Use

### Option 1: Execution Script (Recommended)
```bash
python run_cosgrove_analyzer.py
```

### Option 2: Direct Execution
```bash
python cosgrove_pulse_analyzer.py
```

### Option 3: Streamlit Dashboard
```bash
streamlit run ../dashboards/cosgrove_dashboard.py
```

## 📊 How It Works

### 1. Spreadsheet Reading
- Automatically skips the first 2 rows (section titles)
- Uses row 3 as the real header
- Automatically identifies the "Week Ending" column

### 2. Column Mapping
The system automatically maps columns based on names:

#### 🏠 Occupancy
- `Total Units` → Total units
- `Occupied Units` → Occupied units
- `Vacant-Rented` → Already rented vacancies
- `Vacant-Unrented` → Available vacancies

#### 💰 Financial
- `Monthly Rent` → Monthly rent
- `Net Monthly Income` → Net revenue
- `Delinquency` → Delinquency

#### 👥 Leasing
- `Guest Cards` → Visitor cards
- `Applicants` → Candidates

#### 🏦 Banking
- `CAPEX` → CAPEX account
- `Checking 5026` → Operational account
- `Business Checking 2487` → Main account

### 3. Automatic Calculations
```python
# Physical Occupancy
physical_occupancy = (occupied_units / total_units) * 100

# Pre-Leasing
pre_leased = ((occupied_units + vacant_rented) / total_units) * 100

# Economic Occupancy
economic_occupancy = (net_monthly_income / monthly_rent) * 100

# Closing Ratio
closing_ratio = (applicants / guest_cards) * 100

# Delinquency Variation
delinquency_change = current_delinquency - previous_delinquency
```

## 🔧 Configuration

### File Path
By default, the system looks for the file at:
```
/Users/alexsandersilveira/Downloads/The Cosgrove Pulse- NEXGEN.xlsx
```

To change, edit the file `cosgrove_pulse_analyzer.py` at line:
```python
file_path = "/Users/alexsandersilveira/Downloads/The Cosgrove Pulse- NEXGEN.xlsx"
```

### Total Units
The system assumes 36 units by default. To change, edit the line:
```python
total_units = last_week.get(col_mapping.get('total_units'), 36)  # Default 36
```

## 🐛 Troubleshooting

### Error: "File not found"
- Check if the file path is correct
- Make sure the file exists at the specified location

### Error: "Column 'Week Ending' not found"
- Check if the spreadsheet has the "Week Ending" column
- The system looks for variations like "Week Ending", "week ending", etc.

### Error: "Error loading data"
- Check if the file is not open in Excel
- Make sure the file is not corrupted

## 📈 Next Steps

- [ ] Database integration
- [ ] Automatic email alerts
- [ ] REST API for integration
- [ ] Metrics history
- [ ] Market benchmark comparison

---

**Developed for real estate data analysis with focus on performance and usability** 