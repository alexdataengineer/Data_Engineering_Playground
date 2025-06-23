#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scraper Minimalista de Emails de Clínicas
Versão compatível com Python 3.13 (sem pandas, sem lxml)
"""

import requests
import re
import time
import csv
from bs4 import BeautifulSoup
import logging
from datetime import datetime

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

class MinimalClinicScraper:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        })
        
        self.email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        self.results = []
        
    def extract_emails_from_url(self, url):
        """Extrai emails de uma URL específica"""
        try:
            print(f"Processando: {url}")
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            # Usa o parser HTML nativo do BeautifulSoup (sem lxml)
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
                
                # Remove emails duplicados
                unique_emails = list(set(emails))
                
                return {
                    'url': url,
                    'clinic_name': clinic_name,
                    'emails': unique_emails
                }
            
            return None
            
        except Exception as e:
            print(f"Erro ao processar {url}: {e}")
            return None
    
    def scrape_test_sites(self):
        """Scraping de sites de teste"""
        
        # Sites de teste que geralmente têm emails
        test_sites = [
            "https://httpbin.org/html",
            "https://example.com",
            "https://httpbin.org/headers",
        ]
        
        for site in test_sites:
            try:
                result = self.extract_emails_from_url(site)
                if result:
                    self.results.append(result)
                    print(f"✅ Encontrado: {result['clinic_name']} - {len(result['emails'])} emails")
                else:
                    print(f"❌ Nenhum email encontrado em: {site}")
                
                time.sleep(1)  # Delay entre requisições
                
            except Exception as e:
                print(f"❌ Erro ao processar {site}: {e}")
    
    def scrape_medical_sites(self):
        """Scraping de sites médicos"""
        
        # Sites médicos brasileiros
        medical_sites = [
            "https://www.doctoralia.com.br/",
            "https://www.medicinanet.com.br/",
            "https://www.boaconsulta.com/",
            "https://www.clinicas.com.br/",
        ]
        
        for site in medical_sites:
            try:
                result = self.extract_emails_from_url(site)
                if result:
                    self.results.append(result)
                    print(f"✅ Encontrado: {result['clinic_name']} - {len(result['emails'])} emails")
                else:
                    print(f"❌ Nenhum email encontrado em: {site}")
                
                time.sleep(2)  # Delay maior para sites médicos
                
            except Exception as e:
                print(f"❌ Erro ao processar {site}: {e}")
    
    def save_results_csv(self, filename="clinicas_emails.csv"):
        """Salva os resultados em CSV"""
        if self.results:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['URL', 'Nome da Clínica', 'Email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for result in self.results:
                    for email in result['emails']:
                        writer.writerow({
                            'URL': result['url'],
                            'Nome da Clínica': result['clinic_name'],
                            'Email': email
                        })
            
            print(f"✅ Resultados salvos em {filename}")
            return filename
        else:
            print("⚠️  Nenhum resultado para salvar")
            return None
    
    def save_results_txt(self, filename="clinicas_emails.txt"):
        """Salva os resultados em formato texto simples"""
        if self.results:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=== EMAILS DE CLÍNICAS ENCONTRADOS ===\n")
                f.write(f"Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"Total de clínicas: {len(self.results)}\n\n")
                
                for i, result in enumerate(self.results, 1):
                    f.write(f"{i}. {result['clinic_name']}\n")
                    f.write(f"   URL: {result['url']}\n")
                    f.write(f"   Emails: {', '.join(result['emails'])}\n")
                    f.write("\n")
            
            print(f"✅ Resultados salvos em {filename}")
            return filename
        else:
            print("⚠️  Nenhum resultado para salvar")
            return None

def main():
    """Função principal"""
    print("=" * 60)
    print("🏥 SCRAPER MINIMALISTA DE EMAILS DE CLÍNICAS")
    print("=" * 60)
    print("Versão: Python 3.13 Compatible")
    print("Data:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("=" * 60)
    
    scraper = MinimalClinicScraper()
    
    # 1. Teste com sites básicos
    print("\n1. 🧪 Testando com sites básicos...")
    scraper.scrape_test_sites()
    
    # 2. Scraping de sites médicos
    print("\n2. 🏥 Buscando em sites médicos...")
    scraper.scrape_medical_sites()
    
    # 3. Salva resultados
    print("\n3. 💾 Salvando resultados...")
    csv_file = scraper.save_results_csv()
    txt_file = scraper.save_results_txt()
    
    print(f"\n" + "=" * 60)
    print("📊 RESUMO FINAL")
    print("=" * 60)
    print(f"Total de clínicas encontradas: {len(scraper.results)}")
    total_emails = sum(len(r['emails']) for r in scraper.results)
    print(f"Total de emails: {total_emails}")
    print(f"Arquivo CSV: {csv_file}")
    print(f"Arquivo TXT: {txt_file}")
    
    # Mostra alguns resultados
    if scraper.results:
        print(f"\n📋 PRIMEIROS RESULTADOS:")
        print("-" * 40)
        for i, result in enumerate(scraper.results[:3]):
            print(f"{i+1}. {result['clinic_name']}")
            print(f"   URL: {result['url']}")
            print(f"   Emails: {', '.join(result['emails'])}")
            print()
    else:
        print("\n❌ Nenhum resultado encontrado")
        print("💡 Tente adicionar mais URLs ou verificar a conexão com a internet")

if __name__ == "__main__":
    main() 