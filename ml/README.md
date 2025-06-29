# 🧠 Machine Learning

Collection of machine learning scripts, models, and utilities for data analysis and predictive modeling.

## 🚀 Features

### 📊 ML Components
- **SaaS Company Analysis** - Top 100 SaaS companies analysis
- **Predictive Models** - Various ML algorithms and implementations
- **Data Processing** - Feature engineering and data preparation
- **Model Evaluation** - Performance metrics and validation

### 🎯 Resources
- **Classification Models** - For categorical predictions
- **Regression Models** - For numerical predictions
- **Clustering Algorithms** - For pattern discovery
- **Feature Engineering** - Data transformation utilities
- **Model Deployment** - Production-ready implementations

## 📁 Project Structure

```
ml/
├── top_100_saas_companies_2025..py   # SaaS companies analysis
├── topsaas.py                        # SaaS data processing
└── README.md                         # This file
```

## 🛠️ Installation

### 1. Prerequisites
- Python 3.8 or higher
- Required ML libraries
- Data processing tools

### 2. Install Dependencies
```bash
pip install -r ../requirements.txt
```

### 3. ML-Specific Dependencies
- `scikit-learn` - Machine learning algorithms
- `pandas` - Data manipulation
- `numpy` - Numerical computations
- `matplotlib` - Plotting
- `seaborn` - Statistical visualizations
- `xgboost` - Gradient boosting
- `lightgbm` - Light gradient boosting
- `tensorflow` - Deep learning (optional)
- `pytorch` - Deep learning (optional)

## 🚀 How to Use

### 1. SaaS Companies Analysis
```bash
python top_100_saas_companies_2025..py
```

**Features:**
- Analysis of top SaaS companies
- Market trends identification
- Performance metrics calculation
- Predictive insights

### 2. SaaS Data Processing
```bash
python topsaas.py
```

**Features:**
- Data cleaning and preprocessing
- Feature engineering
- Model training and evaluation
- Results visualization

## 📊 Data Sources

### Primary Sources
- **Company Databases** - SaaS company information
- **Financial APIs** - Market data and metrics
- **Web Scraping** - Company websites and profiles
- **Public Datasets** - Industry benchmarks

### Data Types
- **Company Information** - Size, industry, location
- **Financial Metrics** - Revenue, growth, valuation
- **Market Data** - Stock prices, market cap
- **Performance Indicators** - KPIs and metrics

## 🔧 Configuration

### Model Parameters
```python
# Example configuration
MODEL_CONFIG = {
    'random_forest': {
        'n_estimators': 100,
        'max_depth': 10,
        'random_state': 42
    },
    'xgboost': {
        'n_estimators': 100,
        'max_depth': 6,
        'learning_rate': 0.1
    }
}
```

### Data Paths
```python
# Data storage configuration
DATA_PATHS = {
    'raw_data': './data/raw/',
    'processed_data': './data/processed/',
    'models': './models/',
    'results': './results/'
}
```

## 🤖 Machine Learning Models

### Classification Models
```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

# Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Logistic Regression
lr_model = LogisticRegression(random_state=42)
lr_model.fit(X_train, y_train)

# Support Vector Machine
svm_model = SVC(kernel='rbf', random_state=42)
svm_model.fit(X_train, y_train)
```

### Regression Models
```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

# Random Forest Regression
rf_reg = RandomForestRegressor(n_estimators=100, random_state=42)
rf_reg.fit(X_train, y_train)

# Linear Regression
lr_reg = LinearRegression()
lr_reg.fit(X_train, y_train)

# Support Vector Regression
svr_reg = SVR(kernel='rbf')
svr_reg.fit(X_train, y_train)
```

### Clustering Models
```python
from sklearn.cluster import KMeans, DBSCAN
from sklearn.mixture import GaussianMixture

# K-Means Clustering
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(X)

# DBSCAN Clustering
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan.fit(X)

# Gaussian Mixture
gmm = GaussianMixture(n_components=5, random_state=42)
gmm.fit(X)
```

## 📈 Feature Engineering

### Numerical Features
```python
# Scaling
from sklearn.preprocessing import StandardScaler, MinMaxScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Polynomial features
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
```

### Categorical Features
```python
# One-hot encoding
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder(sparse=False)
X_encoded = encoder.fit_transform(X_categorical)

# Label encoding
from sklearn.preprocessing import LabelEncoder

label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
```

### Time Series Features
```python
# Lag features
df['lag_1'] = df['target'].shift(1)
df['lag_7'] = df['target'].shift(7)

# Rolling statistics
df['rolling_mean_7'] = df['target'].rolling(window=7).mean()
df['rolling_std_7'] = df['target'].rolling(window=7).std()
```

## 📊 Model Evaluation

### Classification Metrics
```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1-Score: {f1:.4f}")
```

### Regression Metrics
```python
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"MSE: {mse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R²: {r2:.4f}")
```

### Cross-Validation
```python
from sklearn.model_selection import cross_val_score

# Perform cross-validation
cv_scores = cross_val_score(model, X, y, cv=5)
print(f"CV Scores: {cv_scores}")
print(f"CV Mean: {cv_scores.mean():.4f}")
print(f"CV Std: {cv_scores.std():.4f}")
```

## 📈 Hyperparameter Tuning

### Grid Search
```python
from sklearn.model_selection import GridSearchCV

# Define parameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [5, 10, 15],
    'min_samples_split': [2, 5, 10]
}

# Perform grid search
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print(f"Best parameters: {grid_search.best_params_}")
print(f"Best score: {grid_search.best_score_:.4f}")
```

### Random Search
```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import uniform, randint

# Define parameter distributions
param_dist = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(3, 20),
    'min_samples_split': randint(2, 20)
}

# Perform random search
random_search = RandomizedSearchCV(RandomForestClassifier(), param_dist, n_iter=100, cv=5)
random_search.fit(X_train, y_train)

print(f"Best parameters: {random_search.best_params_}")
print(f"Best score: {random_search.best_score_:.4f}")
```

## 📊 Visualization

### Model Performance
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()
```

### Feature Importance
```python
# Feature importance for tree-based models
feature_importance = model.feature_importances_
feature_names = X.columns

# Plot feature importance
plt.figure(figsize=(10, 6))
plt.bar(range(len(feature_importance)), feature_importance)
plt.xticks(range(len(feature_importance)), feature_names, rotation=45)
plt.title('Feature Importance')
plt.tight_layout()
plt.show()
```

## 🚀 Model Deployment

### Save and Load Models
```python
import joblib

# Save model
joblib.dump(model, 'model.pkl')

# Load model
loaded_model = joblib.load('model.pkl')

# Make predictions
predictions = loaded_model.predict(X_new)
```

### API Deployment
```python
from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = data['features']
    prediction = model.predict([features])
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
```

## 📈 Next Steps

- [ ] Deep learning models
- [ ] Automated ML pipelines
- [ ] Model monitoring and drift detection
- [ ] A/B testing framework
- [ ] Real-time prediction APIs
- [ ] Model explainability tools

## ⚠️ Considerations

### Data Quality
- **Data Validation** - Ensure data quality
- **Feature Selection** - Choose relevant features
- **Data Leakage** - Avoid information leakage
- **Bias Detection** - Check for model bias

### Model Management
- **Version Control** - Track model versions
- **Reproducibility** - Ensure reproducible results
- **Monitoring** - Monitor model performance
- **Retraining** - Regular model updates

---

**Developed for advanced machine learning applications and insights** 