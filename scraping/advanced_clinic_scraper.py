#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scraper Avançado de Emails de Clínicas e Consultórios
Usa múltiplas fontes e estratégias de busca
"""

import requests
import re
import time
import random
import pandas as pd
from bs4 import BeautifulSoup
import json
import logging
from datetime import datetime
from urllib.parse import urljoin, urlparse, quote_plus
import csv

# Configuração de logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('advanced_scraping.log'),
        logging.StreamHandler()
    ]
)

class AdvancedClinicScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
        self.results = []
        self.visited_urls = set()
        
        # Padrões de email mais robustos
        self.email_patterns = [
            re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'),
        ]
        
        # Palavras-chave médicas
        self.medical_keywords = [
            'clínica', 'consultório', 'médico', 'doutor', 'dr.', 'dra.',
            'especialista', 'cardiologia', 'dermatologia', 'ortopedia',
            'ginecologia', 'pediatria', 'neurologia', 'psiquiatria',
            'odontologia', 'dentista', 'fisioterapia', 'nutrição',
            'endocrinologia', 'urologia', 'oftalmologia', 'otorrinolaringologia',
            'gastroenterologia', 'reumatologia', 'hematologia', 'oncologia'
        ]
        
        # Sites de diretório médico
        self.medical_directories = [
            'https://www.doctoralia.com.br/',
            'https://www.medicinanet.com.br/',
            'https://www.boaconsulta.com/',
            'https://www.medicinanet.com.br/',
            'https://www.doctoralia.com.br/',
            'https://www.medicinanet.com.br/',
            'https://www.boaconsulta.com/',
        ]
        
    def extract_emails_from_text(self, text):
        """Extrai emails usando múltiplos padrões"""
        emails = set()
        for pattern in self.email_patterns:
            found_emails = pattern.findall(text)
            emails.update(found_emails)
        
        # Filtra emails inválidos
        valid_emails = []
        for email in emails:
            if self.is_valid_email(email):
                valid_emails.append(email.lower())
        
        return list(set(valid_emails))
    
    def is_valid_email(self, email):
        """Valida se o email é válido"""
        # Remove emails comuns de spam/teste
        spam_emails = ['test@', 'example@', 'admin@', 'info@', 'noreply@', 'no-reply@']
        return not any(spam in email.lower() for spam in spam_emails)
    
    def is_medical_related(self, text):
        """Verifica se o texto está relacionado à medicina"""
        text_lower = text.lower()
        return any(keyword in text_lower for keyword in self.medical_keywords)
    
    def scrape_medical_directories(self):
        """Scraping de diretórios médicos"""
        logging.info("Iniciando scraping de diretórios médicos...")
        
        for directory in self.medical_directories:
            try:
                logging.info(f"Processando diretório: {directory}")
                
                response = self.session.get(directory, timeout=15)
                response.raise_for_status()
                
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Busca por links de clínicas
                clinic_links = []
                
                # Procura por links que podem ser de clínicas
                for link in soup.find_all('a', href=True):
                    href = link.get('href')
                    text = link.get_text().strip()
                    
                    if href and self.is_medical_related(text):
                        full_url = urljoin(directory, href)
                        clinic_links.append(full_url)
                
                # Processa os links encontrados
                for link in clinic_links[:10]:  # Limita a 10 por diretório
                    if link not in self.visited_urls:
                        self.visited_urls.add(link)
                        result = self.scrape_single_page(link)
                        if result:
                            self.results.append(result)
                            logging.info(f"Encontrado: {result['clinic_name']} - {len(result['emails'])} emails")
                        
                        time.sleep(random.uniform(1, 3))
                
                time.sleep(random.uniform(3, 6))
                
            except Exception as e:
                logging.error(f"Erro ao processar diretório {directory}: {e}")
    
    def scrape_single_page(self, url):
        """Scraping de uma página individual"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove scripts e styles
            for script in soup(["script", "style", "nav", "footer"]):
                script.decompose()
            
            text = soup.get_text()
            emails = self.extract_emails_from_text(text)
            
            if emails and self.is_medical_related(text):
                clinic_name = self.extract_clinic_name(soup, url)
                return {
                    'url': url,
                    'clinic_name': clinic_name,
                    'emails': emails,
                    'source': 'directory'
                }
            
            return None
            
        except Exception as e:
            logging.error(f"Erro ao processar {url}: {e}")
            return None
    
    def extract_clinic_name(self, soup, url):
        """Extrai o nome da clínica de forma mais robusta"""
        # Tenta diferentes estratégias para encontrar o nome
        
        # 1. Título da página
        title = soup.find('title')
        if title:
            title_text = title.get_text().strip()
            if title_text and len(title_text) < 100:
                return title_text
        
        # 2. H1
        h1 = soup.find('h1')
        if h1:
            h1_text = h1.get_text().strip()
            if h1_text and len(h1_text) < 100:
                return h1_text
        
        # 3. Meta tags
        meta_title = soup.find('meta', property='og:title')
        if meta_title:
            meta_text = meta_title.get('content', '').strip()
            if meta_text and len(meta_text) < 100:
                return meta_text
        
        # 4. URL como fallback
        domain = urlparse(url).netloc
        if domain:
            return domain.replace('www.', '')
        
        return "Nome não encontrado"
    
    def search_google_clinics(self, city="São Paulo", state="SP"):
        """Simula busca no Google por clínicas"""
        logging.info(f"Buscando clínicas em {city}, {state}")
        
        # Termos de busca
        search_terms = [
            f"clínicas médicas {city} {state}",
            f"consultórios médicos {city} {state}",
            f"médicos especialistas {city} {state}",
            f"clínicas {city} {state}",
            f"consultório {city} {state}",
        ]
        
        # URLs de exemplo (em um caso real, você faria scraping dos resultados do Google)
        example_clinics = [
            f"https://clinica-exemplo-{city.lower()}.com.br",
            f"https://consultorio-{city.lower()}.com.br",
            f"https://medico-{city.lower()}.com.br",
        ]
        
        for url in example_clinics:
            if url not in self.visited_urls:
                self.visited_urls.add(url)
                result = self.scrape_single_page(url)
                if result:
                    self.results.append(result)
                    logging.info(f"Encontrado via busca: {result['clinic_name']}")
                
                time.sleep(random.uniform(1, 2))
    
    def scrape_from_csv_list(self, csv_file):
        """Scraping de uma lista de URLs em CSV"""
        try:
            with open(csv_file, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    url = row.get('url', '').strip()
                    if url and url not in self.visited_urls:
                        self.visited_urls.add(url)
                        result = self.scrape_single_page(url)
                        if result:
                            self.results.append(result)
                            logging.info(f"Encontrado via CSV: {result['clinic_name']}")
                        
                        time.sleep(random.uniform(1, 2))
        except FileNotFoundError:
            logging.warning(f"Arquivo {csv_file} não encontrado")
        except Exception as e:
            logging.error(f"Erro ao processar CSV {csv_file}: {e}")
    
    def save_results(self, filename=None):
        """Salva os resultados em múltiplos formatos"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"clinicas_avancado_{timestamp}"
        
        if self.results:
            # Prepara dados
            data = []
            for result in self.results:
                for email in result['emails']:
                    data.append({
                        'URL': result['url'],
                        'Nome da Clínica': result['clinic_name'],
                        'Email': email,
                        'Fonte': result.get('source', 'unknown')
                    })
            
            df = pd.DataFrame(data)
            
            # Salva em Excel
            excel_file = f"{filename}.xlsx"
            df.to_excel(excel_file, index=False)
            logging.info(f"Resultados salvos em Excel: {excel_file}")
            
            # Salva em CSV
            csv_file = f"{filename}.csv"
            df.to_csv(csv_file, index=False, encoding='utf-8')
            logging.info(f"Resultados salvos em CSV: {csv_file}")
            
            # Salva estatísticas
            stats_file = f"{filename}_stats.txt"
            with open(stats_file, 'w', encoding='utf-8') as f:
                f.write(f"Estatísticas do Scraping\n")
                f.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total de clínicas: {len(self.results)}\n")
                f.write(f"Total de emails únicos: {len(set([email for r in self.results for email in r['emails']]))}\n")
                f.write(f"URLs processadas: {len(self.visited_urls)}\n")
            
            return excel_file
        else:
            logging.warning("Nenhum resultado para salvar")
            return None

def main():
    """Função principal"""
    print("=== Scraper Avançado de Emails de Clínicas ===")
    print("Iniciando processo de extração avançada...")
    
    scraper = AdvancedClinicScraper()
    
    # 1. Scraping de diretórios médicos
    print("1. Buscando em diretórios médicos...")
    scraper.scrape_medical_directories()
    
    # 2. Busca por cidade
    print("2. Buscando por cidade...")
    cities = [
        ("São Paulo", "SP"),
        ("Rio de Janeiro", "RJ"),
        ("Belo Horizonte", "MG"),
    ]
    
    for city, state in cities:
        scraper.search_google_clinics(city, state)
    
    # 3. Salva resultados
    print("3. Salvando resultados...")
    filename = scraper.save_results()
    
    print(f"\n=== Resumo Final ===")
    print(f"Total de clínicas encontradas: {len(scraper.results)}")
    total_emails = sum(len(r['emails']) for r in scraper.results)
    unique_emails = len(set([email for r in scraper.results for email in r['emails']]))
    print(f"Total de emails: {total_emails}")
    print(f"Emails únicos: {unique_emails}")
    print(f"URLs processadas: {len(scraper.visited_urls)}")
    print(f"Arquivo salvo: {filename}")
    
    # Mostra alguns resultados
    if scraper.results:
        print("\n=== Primeiros Resultados ===")
        for i, result in enumerate(scraper.results[:5]):
            print(f"{i+1}. {result['clinic_name']}")
            print(f"   URL: {result['url']}")
            print(f"   Emails: {', '.join(result['emails'])}")
            print()

if __name__ == "__main__":
    main() 