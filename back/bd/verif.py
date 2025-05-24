import os, sys, psycopg2
from dotenv import load_dotenv

def get_env_path():
    """Retorna o caminho correto para o .env dentro da pasta _internal"""
    if getattr(sys, 'frozen', False):  # Se estiver rodando como executável
        base_path = os.path.join(sys._MEIPASS, "_internal")  # PyInstaller extrai arquivos aqui
    else:
        current_path = os.path.dirname(os.path.abspath(__file__))
        base_path = os.path.abspath(os.path.join(current_path, "..", ".."))   # Caminho do script no desenvolvimento

    return os.path.join(base_path, ".env")  # Retorna o caminho completo do .env

def get_table_path():
    """Retorna o caminho correto para a tabela dentro da pasta _internal"""
    if getattr(sys, 'frozen', False):  # Se estiver rodando como executável
        base_path = os.path.join(sys._MEIPASS, "_internal")  # PyInstaller extrai arquivos aqui
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))  # Caminho do script no desenvolvimento

    return os.path.join(base_path, "Tabelas")  

def versaoApp():
    load_dotenv(get_env_path())

    servidor = psycopg2.connect(
        dbname= os.getenv("DB_NAME"),  # Substitua pelo nome do seu banco de dados
        user= os.getenv("USER"),      # Substitua pelo seu nome de usuário
        password= os.getenv("PASSWORD"),    # Substitua pela sua senha
        host= os.getenv("HOST"),  # Endereço IPv6 do servidor PostgreSQL (Radmin VPN)
        port= os.getenv("PORT") 

    )
    cursor = servidor.cursor()
    cursor.execute("SELECT versao FROM atualizador")
    versao = cursor.fetchall()
    cursor.close()
    versao = versao[0][0]
    if versao == os.getenv("VERSION"):
        return True
    else:
        return False