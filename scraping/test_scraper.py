#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Teste para o Scraper de Clínicas
Testa as funcionalidades básicas
"""

import sys
import os
import requests
from bs4 import BeautifulSoup
import re

def test_dependencies():
    """Testa se todas as dependências estão instaladas"""
    print("🔍 Testando dependências...")
    
    try:
        import requests
        print("✅ requests - OK")
    except ImportError:
        print("❌ requests - FALTANDO")
        return False
    
    try:
        import pandas
        print("✅ pandas - OK")
    except ImportError:
        print("❌ pandas - FALTANDO")
        return False
    
    try:
        from bs4 import BeautifulSoup
        print("✅ beautifulsoup4 - OK")
    except ImportError:
        print("❌ beautifulsoup4 - FALTANDO")
        return False
    
    try:
        from fake_useragent import UserAgent
        print("✅ fake-useragent - OK")
    except ImportError:
        print("❌ fake-useragent - FALTANDO")
        return False
    
    try:
        from selenium import webdriver
        print("✅ selenium - OK")
    except ImportError:
        print("❌ selenium - FALTANDO")
        return False
    
    return True

def test_selenium():
    """Testa se o Selenium está funcionando"""
    print("\n🔍 Testando Selenium...")
    
    try:
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com")
        title = driver.title
        driver.quit()
        
        print(f"✅ Selenium - OK (Título: {title})")
        return True
        
    except Exception as e:
        print(f"❌ Selenium - ERRO: {e}")
        print("💡 Dica: Instale o ChromeDriver")
        return False

def test_email_extraction():
    """Testa a extração de emails"""
    print("\n🔍 Testando extração de emails...")
    
    # Texto de teste com emails
    test_text = """
    Entre em contato conosco:
    Email: contato@clinicaexemplo.com.br
    Telefone: (11) 1234-5678
    Dr. João Silva: joao.silva@clinicaexemplo.com.br
    Dra. Maria Santos: maria.santos@clinicaexemplo.com.br
    """
    
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    emails = email_pattern.findall(test_text)
    
    expected_emails = [
        'contato@clinicaexemplo.com.br',
        'joao.silva@clinicaexemplo.com.br',
        'maria.santos@clinicaexemplo.com.br'
    ]
    
    if set(emails) == set(expected_emails):
        print("✅ Extração de emails - OK")
        print(f"   Emails encontrados: {emails}")
        return True
    else:
        print("❌ Extração de emails - ERRO")
        print(f"   Esperado: {expected_emails}")
        print(f"   Encontrado: {emails}")
        return False

def test_web_request():
    """Testa requisições web"""
    print("\n🔍 Testando requisições web...")
    
    try:
        response = requests.get("https://httpbin.org/get", timeout=10)
        if response.status_code == 200:
            print("✅ Requisições web - OK")
            return True
        else:
            print(f"❌ Requisições web - ERRO (Status: {response.status_code})")
            return False
    except Exception as e:
        print(f"❌ Requisições web - ERRO: {e}")
        return False

def test_file_creation():
    """Testa criação de arquivos"""
    print("\n🔍 Testando criação de arquivos...")
    
    try:
        import pandas as pd
        
        # Cria um DataFrame de teste
        test_data = {
            'URL': ['https://exemplo.com'],
            'Nome da Clínica': ['Clínica Teste'],
            'Email': ['teste@clinica.com']
        }
        
        df = pd.DataFrame(test_data)
        test_file = 'test_output.xlsx'
        df.to_excel(test_file, index=False)
        
        if os.path.exists(test_file):
            os.remove(test_file)  # Remove o arquivo de teste
            print("✅ Criação de arquivos - OK")
            return True
        else:
            print("❌ Criação de arquivos - ERRO")
            return False
            
    except Exception as e:
        print(f"❌ Criação de arquivos - ERRO: {e}")
        return False

def main():
    """Função principal de teste"""
    print("🧪 TESTE DO SCRAPER DE CLÍNICAS")
    print("=" * 50)
    
    tests = [
        test_dependencies,
        test_selenium,
        test_email_extraction,
        test_web_request,
        test_file_creation
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 50)
    print(f"📊 RESULTADO: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram! O scraper está pronto para uso.")
        print("\n💡 Próximos passos:")
        print("1. Execute: python simple_clinic_scraper.py")
        print("2. Ou execute: python clinic_email_scraper.py")
        print("3. Verifique os resultados nos arquivos gerados")
    else:
        print("⚠️  Alguns testes falharam. Verifique as dependências.")
        print("\n💡 Soluções:")
        print("1. Execute: pip install -r requirements.txt")
        print("2. Instale o ChromeDriver")
        print("3. Verifique sua conexão com a internet")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 