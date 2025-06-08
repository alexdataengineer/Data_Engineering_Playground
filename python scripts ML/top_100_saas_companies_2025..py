import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# Caminho do arquivo CSV
csv_path = '/Users/alexsandersilveira/Downloads/top_100_saas_companies_2025.csv'

# Carregar os dados
df = pd.read_csv(csv_path)
print('Colunas:', df.columns.tolist())
print(df.head())

# Pré-processamento simples
# Remover colunas que não ajudam na predição ou são IDs
cols_to_drop = ['Company Name', 'Product', 'Top Investors', 'HQ']
df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])

# Tratar variáveis categóricas
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].fillna('Unknown')
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Tratar valores nulos numéricos
for col in df.select_dtypes(include=['float64', 'int64']).columns:
    df[col] = df[col].fillna(df[col].median())

# Separar variáveis preditoras e alvo
y = df['G2 Rating']
X = df.drop(columns=['G2 Rating'])

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Avaliar
y_pred = model.predict(X_test)
print('MSE:', mean_squared_error(y_test, y_pred))
print('R2:', r2_score(y_test, y_pred))

# Análise descritiva
print('\nResumo estatístico:')
print(df.describe())

print('\nCorrelação com G2 Rating:')
print(df.corr(numeric_only=True)['G2 Rating'].sort_values(ascending=False))

# Se ainda tiver o nome da empresa, mostrar as top 5
if 'Company Name' in df.columns:
    print('\nTop 5 empresas por G2 Rating:')
    print(df[['Company Name', 'G2 Rating']].sort_values(by='G2 Rating', ascending=False).head())

# Importância das variáveis (gráfico em ordem crescente)
importances = model.feature_importances_
feat_names = X.columns
sorted_idx = importances.argsort()
plt.figure(figsize=(10,6))
plt.barh(feat_names[sorted_idx], importances[sorted_idx])
plt.xlabel('Importância')
plt.title('Importância das Variáveis para o G2 Rating (ordem crescente)')
plt.tight_layout()
plt.show()
