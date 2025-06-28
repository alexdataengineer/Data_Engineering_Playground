#!/usr/bin/env python3
"""
Script principal para executar o Cosgrove Pulse Analyzer
"""

import os
import sys
import subprocess
from pathlib import Path

def install_dependencies():
    """Instala as dependências necessárias"""
    print("📦 Instalando dependências...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False

def run_analyzer():
    """Executa o analisador via linha de comando"""
    print("🚀 Executando Cosgrove Pulse Analyzer...")
    
    analyzer_path = "python scripts ML/cosgrove_pulse_analyzer.py"
    
    try:
        subprocess.run([sys.executable, analyzer_path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar analisador: {e}")
    except FileNotFoundError:
        print("❌ Arquivo do analisador não encontrado!")

def run_dashboard():
    """Executa o dashboard Streamlit"""
    print("🌐 Iniciando dashboard Streamlit...")
    
    dashboard_path = "streamlit/cosgrove_dashboard.py"
    
    try:
        # Inicia o Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", dashboard_path,
            "--server.port", "8501",
            "--server.address", "localhost"
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao executar dashboard: {e}")
    except FileNotFoundError:
        print("❌ Arquivo do dashboard não encontrado!")

def main():
    """Função principal"""
    print("🚀 COSGROVE PULSE ANALYZER - LAUNCHER")
    print("=" * 50)
    
    # Verifica se estamos no diretório correto
    if not os.path.exists("requirements.txt"):
        print("❌ Arquivo requirements.txt não encontrado!")
        print("Certifique-se de estar no diretório raiz do projeto.")
        return
    
    # Menu principal
    while True:
        print("\n🤔 Escolha uma opção:")
        print("1. 📦 Instalar/Atualizar dependências")
        print("2. 🚀 Executar analisador (linha de comando)")
        print("3. 🌐 Executar dashboard (Streamlit)")
        print("4. ❌ Sair")
        
        choice = input("\nEscolha uma opção (1-4): ").strip()
        
        if choice == "1":
            install_dependencies()
        elif choice == "2":
            run_analyzer()
        elif choice == "3":
            run_dashboard()
        elif choice == "4":
            print("👋 Até logo!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main() 