import os
import sys

def get_env_path():
    """Retorna o caminho correto para o .env dentro da pasta _internal"""
    if getattr(sys, 'frozen', False):  # Se estiver rodando como executável
        base_path = os.path.join(sys._MEIPASS, "_internal")  # PyInstaller extrai arquivos aqui
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))  # Caminho do script no desenvolvimento

    return os.path.join(base_path, ".env")  # Retorna o caminho completo do .env

def get_table_path():
    """Retorna o caminho correto para a tabela dentro da pasta _internal"""
    if getattr(sys, 'frozen', False):  # Se estiver rodando como executável
        base_path = os.path.join(sys._MEIPASS, "_internal")  # PyInstaller extrai arquivos aqui
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))  # Caminho do script no desenvolvimento

    return os.path.join(base_path, "Tabelas")  # Retorna o caminho completo da tabela