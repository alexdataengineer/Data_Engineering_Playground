#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configurações para o Scraper de Emails de Clínicas
"""

# Configurações gerais
SETTINGS = {
    'delay_between_requests': (1, 3),  # Delay aleatório entre requisições (min, max)
    'timeout': 10,  # Timeout para requisições
    'max_results_per_search': 20,  # Máximo de resultados por busca
    'max_pages_per_city': 5,  # Máximo de páginas por cidade
}

# Cidades para buscar (você pode adicionar mais)
CITIES = [
    ("São Paulo", "SP"),
    ("Rio de Janeiro", "RJ"),
    ("Belo Horizonte", "MG"),
    ("Brasília", "DF"),
    ("Salvador", "BA"),
    ("Fortaleza", "CE"),
    ("Curitiba", "PR"),
    ("Porto Alegre", "RS"),
    ("Recife", "PE"),
    ("Goiânia", "GO"),
    ("Manaus", "AM"),
    ("Belém", "PA"),
    ("Vitória", "ES"),
    ("Campo Grande", "MS"),
    ("Cuiabá", "MT"),
]

# Especialidades médicas para busca
MEDICAL_SPECIALTIES = [
    "cardiologia",
    "dermatologia", 
    "ortopedia",
    "ginecologia",
    "pediatria",
    "neurologia",
    "psiquiatria",
    "odontologia",
    "fisioterapia",
    "nutrição",
    "endocrinologia",
    "urologia",
    "oftalmologia",
    "otorrinolaringologia",
    "gastroenterologia",
    "reumatologia",
    "hematologia",
    "oncologia",
    "radiologia",
    "anestesiologia"
]

# Sites de diretório médico
MEDICAL_DIRECTORIES = [
    "https://www.doctoralia.com.br/",
    "https://www.medicinanet.com.br/",
    "https://www.boaconsulta.com/",
    "https://www.medicinanet.com.br/",
    "https://www.doctoralia.com.br/",
    "https://www.medicinanet.com.br/",
    "https://www.boaconsulta.com/",
]

# Termos de busca para clínicas
SEARCH_TERMS = [
    "clínicas médicas",
    "consultórios médicos", 
    "médicos especialistas",
    "clínicas",
    "consultório",
    "especialista médico",
    "doutor",
    "dra.",
    "dr.",
]

# Padrões de email para filtrar (emails que devem ser ignorados)
SPAM_EMAIL_PATTERNS = [
    'test@',
    'example@',
    'admin@',
    'info@',
    'noreply@',
    'no-reply@',
    'webmaster@',
    'postmaster@',
    'mailer-daemon@',
    'abuse@',
]

# User Agents para rotação
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/121.0',
]

# Configurações de output
OUTPUT_CONFIG = {
    'excel_filename': 'clinicas_emails_{timestamp}.xlsx',
    'csv_filename': 'clinicas_emails_{timestamp}.csv',
    'log_filename': 'scraping_{timestamp}.log',
    'include_timestamp': True,
    'save_multiple_formats': True,
}

# Configurações de proxy (opcional)
PROXY_CONFIG = {
    'use_proxy': False,
    'proxy_list': [
        # 'http://proxy1:port',
        # 'http://proxy2:port',
    ],
    'rotate_proxies': True,
}

# Configurações de Selenium
SELENIUM_CONFIG = {
    'headless': True,
    'window_size': (1920, 1080),
    'disable_images': True,
    'disable_javascript': False,
    'page_load_timeout': 30,
    'implicit_wait': 10,
} 