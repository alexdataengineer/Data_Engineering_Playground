# Scraper de Emails de Clínicas e Consultórios Médicos

Este projeto contém scripts Python para extrair emails de clínicas, consultórios e profissionais de saúde de diferentes fontes na web.

## 📋 Índice

- [Instalação](#instalação)
- [Scripts Disponíveis](#scripts-disponíveis)
- [Como Usar](#como-usar)
- [Configuração](#configuração)
- [Funcionalidades](#funcionalidades)
- [Avisos Legais](#avisos-legais)
- [Troubleshooting](#troubleshooting)

## 🚀 Instalação

### 1. Instalar Dependências

```bash
cd scraping
pip install -r requirements.txt
```

### 2. Instalar ChromeDriver (para Selenium)

Para usar o Selenium, você precisa do ChromeDriver:

**macOS:**
```bash
brew install chromedriver
```

**Ubuntu/Debian:**
```bash
sudo apt-get install chromium-chromedriver
```

**Windows:**
Baixe de: https://chromedriver.chromium.org/

## 📁 Scripts Disponíveis

### 1. `clinic_email_scraper.py` - Scraper Principal
- **Funcionalidade**: Scraping completo com Selenium e requests
- **Recursos**: Busca por cidade, extração de URLs, validação de emails
- **Uso**: Para extrações em larga escala

### 2. `simple_clinic_scraper.py` - Scraper Simples
- **Funcionalidade**: Versão mais direta e rápida
- **Recursos**: Foco em sites de diretório médico
- **Uso**: Para extrações rápidas e simples

### 3. `advanced_clinic_scraper.py` - Scraper Avançado
- **Funcionalidade**: Múltiplas fontes e estratégias
- **Recursos**: Validação robusta, múltiplos formatos de saída
- **Uso**: Para extrações profissionais

## 🎯 Como Usar

### Execução Básica

```bash
# Scraper principal
python clinic_email_scraper.py

# Scraper simples
python simple_clinic_scraper.py

# Scraper avançado
python advanced_clinic_scraper.py
```

### Execução Personalizada

```python
from clinic_email_scraper import ClinicEmailScraper

# Criar instância
scraper = ClinicEmailScraper()

# Definir cidades específicas
cities = [
    ("São Paulo", "SP"),
    ("Rio de Janeiro", "RJ"),
    ("Belo Horizonte", "MG"),
]

# Executar scraping
results = scraper.run_scraping(cities, max_pages_per_city=3)

# Salvar resultados
filename = scraper.save_results()
```

## ⚙️ Configuração

### Arquivo `config.py`

Você pode personalizar as configurações editando o arquivo `config.py`:

```python
# Adicionar mais cidades
CITIES = [
    ("Sua Cidade", "UF"),
    # ... outras cidades
]

# Adicionar especialidades médicas
MEDICAL_SPECIALTIES = [
    "sua_especialidade",
    # ... outras especialidades
]

# Configurar delays
SETTINGS = {
    'delay_between_requests': (2, 5),  # Delay maior
    'max_pages_per_city': 10,  # Mais páginas por cidade
}
```

### Configurações Importantes

- **`delay_between_requests`**: Delay entre requisições para evitar bloqueios
- **`max_pages_per_city`**: Número máximo de páginas por cidade
- **`timeout`**: Timeout para requisições HTTP
- **`headless`**: Executar Selenium em modo headless (sem interface gráfica)

## 🔧 Funcionalidades

### ✅ Recursos Implementados

- **Extração de Emails**: Regex robusto para encontrar emails válidos
- **Validação de Conteúdo**: Filtra apenas páginas relacionadas à medicina
- **Múltiplas Fontes**: Diretórios médicos, busca Google, sites específicos
- **Rotação de User Agents**: Evita detecção de bot
- **Delays Aleatórios**: Comportamento mais humano
- **Logs Detalhados**: Acompanhamento do progresso
- **Múltiplos Formatos**: Excel, CSV, logs
- **Tratamento de Erros**: Continua mesmo com falhas
- **Deduplicação**: Remove emails duplicados

### 🎯 Estratégias de Busca

1. **Diretórios Médicos**: Sites como Doctoralia, MedicinaNet
2. **Busca por Cidade**: Termos específicos por localização
3. **Especialidades**: Busca por especialidades médicas
4. **Sites Específicos**: URLs conhecidas de clínicas

### 📊 Output

Os resultados são salvos em:

- **Excel** (`.xlsx`): Formato principal com todas as informações
- **CSV** (`.csv`): Formato simples para análise
- **Logs** (`.log`): Registro detalhado da execução
- **Estatísticas** (`.txt`): Resumo dos resultados

## ⚠️ Avisos Legais

### Importante!

1. **Respeite os Termos de Serviço**: Verifique os termos de cada site antes do scraping
2. **Rate Limiting**: Use delays apropriados para não sobrecarregar servidores
3. **Robots.txt**: Respeite o arquivo robots.txt dos sites
4. **Uso Responsável**: Use os dados apenas para fins legítimos
5. **LGPD**: Respeite a Lei Geral de Proteção de Dados

### Recomendações

- Use delays de pelo menos 1-3 segundos entre requisições
- Limite o número de páginas por site
- Monitore os logs para detectar bloqueios
- Use proxies se necessário (configurável)

## 🔍 Troubleshooting

### Problemas Comuns

#### 1. Erro de ChromeDriver
```
WebDriverException: Message: unknown error: cannot find Chrome binary
```

**Solução:**
```bash
# Instalar Chrome
# macOS
brew install google-chrome

# Ubuntu
sudo apt-get install google-chrome-stable
```

#### 2. Timeout nas Requisições
```
requests.exceptions.Timeout
```

**Solução:**
- Aumentar o timeout no `config.py`
- Verificar conexão com internet
- Usar delays maiores

#### 3. Poucos Resultados
**Possíveis Causas:**
- Sites bloqueando requisições
- Padrões de email muito restritivos
- Palavras-chave muito específicas

**Soluções:**
- Usar User Agents diferentes
- Ajustar padrões de email
- Adicionar mais termos de busca

#### 4. Erro de Dependências
```
ModuleNotFoundError: No module named 'selenium'
```

**Solução:**
```bash
pip install -r requirements.txt
```

### Logs e Debug

Os scripts geram logs detalhados:

```bash
# Ver logs em tempo real
tail -f scraping.log

# Ver logs avançados
tail -f advanced_scraping.log
```

## 📈 Exemplos de Uso

### Exemplo 1: Busca Rápida
```bash
python simple_clinic_scraper.py
```

### Exemplo 2: Busca Completa
```bash
python clinic_email_scraper.py
```

### Exemplo 3: Busca Personalizada
```python
from advanced_clinic_scraper import AdvancedClinicScraper

scraper = AdvancedClinicScraper()

# Buscar apenas em São Paulo
scraper.search_google_clinics("São Paulo", "SP")

# Salvar resultados
scraper.save_results("sao_paulo_clinicas.xlsx")
```

## 🤝 Contribuição

Para contribuir com o projeto:

1. Fork o repositório
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📞 Suporte

Se encontrar problemas:

1. Verifique os logs de erro
2. Consulte a seção Troubleshooting
3. Verifique se todas as dependências estão instaladas
4. Teste com configurações mais conservadoras

## 📄 Licença

Este projeto é para uso educacional e de pesquisa. Use responsavelmente e respeite os termos de serviço dos sites acessados. 