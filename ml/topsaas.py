import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Caminho do arquivo CSV
csv_path = '/Users/alexsandersilveira/Downloads/top_100_saas_companies_2025.csv'

# Carregar os dados
df = pd.read_csv(csv_path)

# Pré-processamento simples
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

# 1. Distribuição do G2 Rating
plt.figure(figsize=(8,5))
sns.histplot(y, bins=10, kde=True)
plt.title('Distribuição do G2 Rating')
plt.xlabel('G2 Rating')
plt.ylabel('Frequência')
plt.tight_layout()
plt.show()

# 2. G2 Rating por Ano de Fundação
plt.figure(figsize=(10,5))
sns.boxplot(x=df['Founded Year'], y=y)
plt.title('G2 Rating por Ano de Fundação')
plt.xlabel('Ano de Fundação')
plt.ylabel('G2 Rating')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3. G2 Rating por Indústria (se existir)
if 'Industry' in df.columns:
    plt.figure(figsize=(12,5))
    sns.boxplot(x=df['Industry'], y=y)
    plt.title('G2 Rating por Indústria')
    plt.xlabel('Indústria')
    plt.ylabel('G2 Rating')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# 4. Top 10 empresas por ARR, Valuation, Funding (se existirem as colunas)
for col in ['ARR', 'Valuation', 'Total Funding']:
    if col in df.columns:
        print(f'\nTop 10 empresas por {col}:')
        if 'Company Name' in df.columns:
            print(df[['Company Name', col, 'G2 Rating']].sort_values(by=col, ascending=False).head(10))
        else:
            print(df[[col, 'G2 Rating']].sort_values(by=col, ascending=False).head(10))

# 5. Scatterplots: ARR, Valuation, Funding vs G2 Rating
for col in ['ARR', 'Valuation', 'Total Funding']:
    if col in df.columns:
        plt.figure(figsize=(8,5))
        plt.scatter(df[col], y)
        plt.title(f'G2 Rating vs {col}')
        plt.xlabel(col)
        plt.ylabel('G2 Rating')
        plt.tight_layout()
        plt.show()

# 6. Heatmap de correlação
plt.figure(figsize=(8,6))
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap de Correlação')
plt.tight_layout()
plt.show() 