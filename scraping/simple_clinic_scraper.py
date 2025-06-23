#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scraper Simples de Emails de Clínicas
Versão mais direta e rápida
"""

import requests
import re
import time
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class SimpleClinicScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        })
        
        self.email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        self.results = []
        
    def extract_emails_from_url(self, url):
        """Extrai emails de uma URL específica"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Remove scripts e styles
            for script in soup(["script", "style"]):
                script.decompose()
            
            text = soup.get_text()
            emails = self.email_pattern.findall(text)
            
            if emails:
                # Tenta extrair o nome da clínica
                title = soup.find('title')
                clinic_name = title.get_text().strip() if title else "Nome não encontrado"
                
                return {
                    'url': url,
                    'clinic_name': clinic_name,
                    'emails': list(set(emails))  # Remove duplicatas
                }
            
            return None
            
        except Exception as e:
            logging.error(f"Erro ao processar {url}: {e}")
            return None
    
    def scrape_from_directory_sites(self):
        """Scraping de sites de diretório de clínicas"""
        
        # Lista de sites de diretório de clínicas
        directory_sites = [
            "https://www.doctoralia.com.br/",
            "https://www.medicinanet.com.br/",
            "https://www.boaconsulta.com/",
            "https://www.doctoralia.com.br/",
            "https://www.medicinanet.com.br/",
        ]
        
        for site in directory_sites:
            try:
                logging.info(f"Processando site: {site}")
                result = self.extract_emails_from_url(site)
                if result:
                    self.results.append(result)
                    logging.info(f"Encontrado: {result['clinic_name']} - {len(result['emails'])} emails")
                
                time.sleep(2)  # Delay entre requisições
                
            except Exception as e:
                logging.error(f"Erro ao processar {site}: {e}")
    
    def scrape_from_google_search(self, query, max_results=20):
        """Scraping baseado em busca do Google"""
        
        # Simula busca do Google (você pode expandir isso)
        search_terms = [
            f"{query} site:clinicamedica.com.br",
            f"{query} site:consultorio.com.br",
            f"{query} site:medicina.com.br",
        ]
        
        for term in search_terms:
            logging.info(f"Buscando: {term}")
            # Aqui você pode implementar busca real no Google
            # Por enquanto, vamos usar URLs conhecidas
            
            # URLs de exemplo de clínicas (você pode expandir esta lista)
            example_urls = [
                "https://exemplo-clinica.com.br",
                "https://consultorio-exemplo.com.br",
                "https://clinica-medica.com.br",
            ]
            
            for url in example_urls:
                result = self.extract_emails_from_url(url)
                if result:
                    self.results.append(result)
                    logging.info(f"Encontrado: {result['clinic_name']} - {len(result['emails'])} emails")
                
                time.sleep(1)
    
    def save_results(self, filename="clinicas_emails.xlsx"):
        """Salva os resultados em Excel"""
        if self.results:
            data = []
            for result in self.results:
                for email in result['emails']:
                    data.append({
                        'URL': result['url'],
                        'Nome da Clínica': result['clinic_name'],
                        'Email': email
                    })
            
            df = pd.DataFrame(data)
            df.to_excel(filename, index=False)
            logging.info(f"Resultados salvos em {filename}")
            return filename
        else:
            logging.warning("Nenhum resultado para salvar")
            return None

def main():
    """Função principal"""
    print("=== Scraper Simples de Emails de Clínicas ===")
    
    scraper = SimpleClinicScraper()
    
    # 1. Scraping de sites de diretório
    print("1. Buscando em sites de diretório...")
    scraper.scrape_from_directory_sites()
    
    # 2. Scraping baseado em busca
    print("2. Buscando clínicas específicas...")
    queries = ["clínica médica", "consultório médico", "especialista médico"]
    for query in queries:
        scraper.scrape_from_google_search(query)
    
    # 3. Salva resultados
    print("3. Salvando resultados...")
    filename = scraper.save_results()
    
    print(f"\n=== Resumo ===")
    print(f"Total de clínicas encontradas: {len(scraper.results)}")
    total_emails = sum(len(r['emails']) for r in scraper.results)
    print(f"Total de emails: {total_emails}")
    print(f"Arquivo salvo: {filename}")

if __name__ == "__main__":
    main() 