#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scraper de Emails de Clínicas e Consultórios Médicos
Autor: Assistente IA
Data: 2024
"""

import requests
import re
import time
import random
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from fake_useragent import UserAgent
import logging
from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraping.log'),
        logging.StreamHandler()
    ]
)

class ClinicEmailScraper:
    def __init__(self):
        self.ua = UserAgent()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': self.ua.random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
        self.results = []
        self.visited_urls = set()
        
        # Padrões de email
        self.email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        
        # Palavras-chave para identificar clínicas
        self.clinic_keywords = [
            'clínica', 'consultório', 'médico', 'doutor', 'dr.', 'dra.',
            'especialista', 'cardiologia', 'dermatologia', 'ortopedia',
            'ginecologia', 'pediatria', 'neurologia', 'psiquiatria',
            'odontologia', 'dentista', 'fisioterapia', 'nutrição'
        ]
        
    def setup_selenium(self):
        """Configura o driver do Selenium para sites dinâmicos"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument(f'--user-agent={self.ua.random}')
        
        try:
            driver = webdriver.Chrome(options=chrome_options)
            return driver
        except Exception as e:
            logging.error(f"Erro ao configurar Selenium: {e}")
            return None
    
    def is_clinic_related(self, text):
        """Verifica se o texto está relacionado a clínicas"""
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.clinic_keywords)
    
    def extract_emails_from_text(self, text):
        """Extrai emails de um texto"""
        emails = self.email_pattern.findall(text)
        return list(set(emails))  # Remove duplicatas
    
    def scrape_page_with_requests(self, url):
        """Scraping usando requests para sites estáticos"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove scripts e styles
            for script in soup(["script", "style"]):
                script.decompose()
            
            text = soup.get_text()
            emails = self.extract_emails_from_text(text)
            
            # Verifica se é relacionado a clínicas
            if self.is_clinic_related(text) and emails:
                clinic_name = self.extract_clinic_name(soup)
                return {
                    'url': url,
                    'clinic_name': clinic_name,
                    'emails': emails,
                    'method': 'requests'
                }
            
            return None
            
        except Exception as e:
            logging.error(f"Erro ao fazer scraping de {url}: {e}")
            return None
    
    def scrape_page_with_selenium(self, url, driver):
        """Scraping usando Selenium para sites dinâmicos"""
        try:
            driver.get(url)
            time.sleep(random.uniform(2, 5))  # Delay aleatório
            
            # Aguarda carregamento da página
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            
            # Remove scripts e styles
            for script in soup(["script", "style"]):
                script.decompose()
            
            text = soup.get_text()
            emails = self.extract_emails_from_text(text)
            
            # Verifica se é relacionado a clínicas
            if self.is_clinic_related(text) and emails:
                clinic_name = self.extract_clinic_name(soup)
                return {
                    'url': url,
                    'clinic_name': clinic_name,
                    'emails': emails,
                    'method': 'selenium'
                }
            
            return None
            
        except Exception as e:
            logging.error(f"Erro ao fazer scraping com Selenium de {url}: {e}")
            return None
    
    def extract_clinic_name(self, soup):
        """Extrai o nome da clínica da página"""
        # Tenta diferentes seletores para encontrar o nome
        selectors = [
            'h1', 'h2', '.clinic-name', '.business-name', '.company-name',
            'title', '.title', '[class*="name"]', '[id*="name"]'
        ]
        
        for selector in selectors:
            elements = soup.select(selector)
            for element in elements:
                text = element.get_text().strip()
                if text and len(text) < 100:  # Nome não muito longo
                    return text
        
        return "Nome não encontrado"
    
    def get_clinic_urls_from_search(self, city="São Paulo", state="SP"):
        """Gera URLs de busca para clínicas"""
        search_urls = [
            f"https://www.google.com/search?q=clínicas+médicas+{city}+{state}",
            f"https://www.google.com/search?q=consultórios+médicos+{city}+{state}",
            f"https://www.google.com/search?q=médicos+especialistas+{city}+{state}",
            f"https://www.google.com/search?q=clínicas+{city}+{state}",
            f"https://www.google.com/search?q=consultório+{city}+{state}",
        ]
        return search_urls
    
    def extract_urls_from_search_results(self, search_url, driver):
        """Extrai URLs dos resultados de busca"""
        try:
            driver.get(search_url)
            time.sleep(random.uniform(3, 6))
            
            # Encontra links dos resultados
            links = driver.find_elements(By.CSS_SELECTOR, 'a[href^="http"]')
            urls = []
            
            for link in links:
                href = link.get_attribute('href')
                if href and 'google.com' not in href:
                    urls.append(href)
            
            return urls[:10]  # Limita a 10 URLs por busca
            
        except Exception as e:
            logging.error(f"Erro ao extrair URLs de {search_url}: {e}")
            return []
    
    def save_results(self, filename=None):
        """Salva os resultados em arquivo Excel"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"clinicas_emails_{timestamp}.xlsx"
        
        if self.results:
            # Prepara dados para o DataFrame
            data = []
            for result in self.results:
                for email in result['emails']:
                    data.append({
                        'URL': result['url'],
                        'Nome da Clínica': result['clinic_name'],
                        'Email': email,
                        'Método': result['method']
                    })
            
            df = pd.DataFrame(data)
            df.to_excel(filename, index=False)
            logging.info(f"Resultados salvos em {filename}")
            return filename
        else:
            logging.warning("Nenhum resultado para salvar")
            return None
    
    def run_scraping(self, cities=None, max_pages_per_city=5):
        """Executa o scraping principal"""
        if cities is None:
            cities = [
                ("São Paulo", "SP"),
                ("Rio de Janeiro", "RJ"),
                ("Belo Horizonte", "MG"),
                ("Brasília", "DF"),
                ("Salvador", "BA"),
                ("Fortaleza", "CE"),
                ("Curitiba", "PR"),
                ("Porto Alegre", "RS"),
                ("Recife", "PE"),
                ("Goiânia", "GO")
            ]
        
        driver = self.setup_selenium()
        
        try:
            for city, state in cities:
                logging.info(f"Iniciando scraping para {city}, {state}")
                
                search_urls = self.get_clinic_urls_from_search(city, state)
                
                for search_url in search_urls[:max_pages_per_city]:
                    if driver:
                        urls = self.extract_urls_from_search_results(search_url, driver)
                        
                        for url in urls:
                            if url not in self.visited_urls:
                                self.visited_urls.add(url)
                                
                                # Tenta primeiro com requests
                                result = self.scrape_page_with_requests(url)
                                
                                # Se não funcionar, tenta com Selenium
                                if not result and driver:
                                    result = self.scrape_page_with_selenium(url, driver)
                                
                                if result:
                                    self.results.append(result)
                                    logging.info(f"Encontrado: {result['clinic_name']} - {len(result['emails'])} emails")
                                
                                # Delay para não sobrecarregar os servidores
                                time.sleep(random.uniform(1, 3))
                
                logging.info(f"Concluído scraping para {city}, {state}. Total: {len(self.results)} clínicas encontradas")
        
        finally:
            if driver:
                driver.quit()
        
        return self.results

def main():
    """Função principal"""
    print("=== Scraper de Emails de Clínicas e Consultórios ===")
    print("Iniciando processo de extração...")
    
    scraper = ClinicEmailScraper()
    
    # Lista de cidades para buscar (você pode modificar)
    cities = [
        ("São Paulo", "SP"),
        ("Rio de Janeiro", "RJ"),
        ("Belo Horizonte", "MG"),
        ("Brasília", "DF"),
        ("Salvador", "BA"),
    ]
    
    # Executa o scraping
    results = scraper.run_scraping(cities, max_pages_per_city=3)
    
    # Salva os resultados
    filename = scraper.save_results()
    
    print(f"\n=== Resumo ===")
    print(f"Total de clínicas encontradas: {len(results)}")
    print(f"Total de emails únicos: {len(set([email for r in results for email in r['emails']]))}")
    print(f"Arquivo salvo: {filename}")
    
    # Mostra alguns resultados
    if results:
        print("\n=== Primeiros Resultados ===")
        for i, result in enumerate(results[:5]):
            print(f"{i+1}. {result['clinic_name']}")
            print(f"   URL: {result['url']}")
            print(f"   Emails: {', '.join(result['emails'])}")
            print()

if __name__ == "__main__":
    main() 