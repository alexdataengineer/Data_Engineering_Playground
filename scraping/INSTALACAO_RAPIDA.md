# 🚀 Instalação Rápida - Scraper de Clínicas

## ⚡ Comece em 3 Passos

### 1. Instalar Dependências
```bash
cd scraping
pip install -r requirements.txt
```

### 2. Testar o Sistema
```bash
python test_scraper.py
```

### 3. Executar o Scraper
```bash
python run_scraper.py
```

## 🎯 Opções de Execução

### Opção A: Interface Interativa (Recomendado)
```bash
python run_scraper.py
```
- Menu interativo
- Escolha o tipo de scraper
- Mais fácil de usar

### Opção B: Scraper Simples (Rápido)
```bash
python simple_clinic_scraper.py
```
- Mais rápido
- Menos recursos
- Ideal para testes

### Opção C: Scraper Principal (Completo)
```bash
python clinic_email_scraper.py
```
- Funcionalidades completas
- Selenium + Requests
- Busca por cidade

### Opção D: Scraper Avançado (Profissional)
```bash
python advanced_clinic_scraper.py
```
- Múltiplas fontes
- Validação robusta
- Múltiplos formatos de saída

## 📊 Resultados

Os emails serão salvos em:
- `clinicas_emails_YYYYMMDD_HHMMSS.xlsx` (Excel)
- `clinicas_emails_YYYYMMDD_HHMMSS.csv` (CSV)
- `scraping.log` (Logs)

## ⚠️ Problemas Comuns

### Erro: "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Erro: "ChromeDriver not found"
**macOS:**
```bash
brew install chromedriver
```

**Ubuntu:**
```bash
sudo apt-get install chromium-chromedriver
```

**Windows:**
Baixe de: https://chromedriver.chromium.org/

### Poucos Resultados
- Aumente os delays no `config.py`
- Use o scraper avançado
- Verifique os logs

## 🔧 Configuração Rápida

Edite `config.py` para personalizar:

```python
# Adicionar sua cidade
CITIES = [
    ("Sua Cidade", "UF"),
    # ... outras cidades
]

# Ajustar delays
SETTINGS = {
    'delay_between_requests': (2, 5),  # Delay maior
    'max_pages_per_city': 10,  # Mais páginas
}
```

## 📞 Suporte Rápido

1. **Teste primeiro**: `python test_scraper.py`
2. **Use o simples**: `python simple_clinic_scraper.py`
3. **Verifique logs**: Arquivos `.log` gerados
4. **Ajuste configurações**: Edite `config.py`

## 🎉 Pronto!

Agora você pode extrair emails de clínicas e consultórios médicos!

**Lembre-se**: Use responsavelmente e respeite os termos de serviço dos sites. 