#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Inicialização Rápida do Scraper de Clínicas
Interface simples para executar o scraper
"""

import sys
import os
from datetime import datetime

def print_banner():
    """Imprime o banner do scraper"""
    print("=" * 60)
    print("🏥 SCRAPER DE EMAILS DE CLÍNICAS E CONSULTÓRIOS")
    print("=" * 60)
    print("Versão: 1.0")
    print("Data:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    print("=" * 60)

def show_menu():
    """Mostra o menu de opções"""
    print("\n📋 ESCOLHA UMA OPÇÃO:")
    print("1. 🧪 Testar sistema (recomendado primeiro)")
    print("2. 🚀 Scraper Simples (rápido)")
    print("3. 🔧 Scraper Principal (completo)")
    print("4. ⚡ Scraper Avançado (profissional)")
    print("5. 📖 Ver documentação")
    print("6. ❌ Sair")
    print("-" * 60)

def run_test():
    """Executa o teste do sistema"""
    print("\n🧪 Executando teste do sistema...")
    try:
        os.system("python test_scraper.py")
    except Exception as e:
        print(f"❌ Erro ao executar teste: {e}")

def run_simple_scraper():
    """Executa o scraper simples"""
    print("\n🚀 Executando scraper simples...")
    print("💡 Este é o mais rápido e seguro para começar")
    try:
        os.system("python simple_clinic_scraper.py")
    except Exception as e:
        print(f"❌ Erro ao executar scraper simples: {e}")

def run_main_scraper():
    """Executa o scraper principal"""
    print("\n🔧 Executando scraper principal...")
    print("⚠️  Este pode demorar mais e usar mais recursos")
    try:
        os.system("python clinic_email_scraper.py")
    except Exception as e:
        print(f"❌ Erro ao executar scraper principal: {e}")

def run_advanced_scraper():
    """Executa o scraper avançado"""
    print("\n⚡ Executando scraper avançado...")
    print("🎯 Este é o mais completo e profissional")
    try:
        os.system("python advanced_clinic_scraper.py")
    except Exception as e:
        print(f"❌ Erro ao executar scraper avançado: {e}")

def show_documentation():
    """Mostra informações sobre o projeto"""
    print("\n📖 DOCUMENTAÇÃO:")
    print("-" * 40)
    print("📁 Arquivos importantes:")
    print("   • README.md - Documentação completa")
    print("   • requirements.txt - Dependências")
    print("   • config.py - Configurações")
    print("   • test_scraper.py - Testes do sistema")
    print("\n🚀 Como usar:")
    print("   1. Instale as dependências: pip install -r requirements.txt")
    print("   2. Execute o teste: python test_scraper.py")
    print("   3. Execute um scraper: python simple_clinic_scraper.py")
    print("\n📊 Resultados:")
    print("   • Arquivos Excel (.xlsx) com os emails")
    print("   • Arquivos CSV (.csv) para análise")
    print("   • Logs (.log) para debug")
    print("\n⚠️  Avisos:")
    print("   • Use responsavelmente")
    print("   • Respeite os termos de serviço")
    print("   • Use delays apropriados")

def check_dependencies():
    """Verifica se as dependências estão instaladas"""
    print("\n🔍 Verificando dependências...")
    try:
        import requests
        import pandas
        from bs4 import BeautifulSoup
        from fake_useragent import UserAgent
        print("✅ Dependências básicas - OK")
        return True
    except ImportError as e:
        print(f"❌ Dependência faltando: {e}")
        print("💡 Execute: pip install -r requirements.txt")
        return False

def main():
    """Função principal"""
    print_banner()
    
    # Verifica dependências
    if not check_dependencies():
        print("\n❌ Instale as dependências primeiro!")
        return
    
    while True:
        show_menu()
        
        try:
            choice = input("Digite sua escolha (1-6): ").strip()
            
            if choice == "1":
                run_test()
            elif choice == "2":
                run_simple_scraper()
            elif choice == "3":
                run_main_scraper()
            elif choice == "4":
                run_advanced_scraper()
            elif choice == "5":
                show_documentation()
            elif choice == "6":
                print("\n👋 Obrigado por usar o Scraper de Clínicas!")
                break
            else:
                print("❌ Opção inválida. Digite 1-6.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Interrompido pelo usuário. Até logo!")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main() 