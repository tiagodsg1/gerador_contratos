import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv
import os
class GetDados():
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        load_dotenv()
        self.servidor = psycopg2.connect(
            dbname= os.getenv("DB_NAME"),  # Substitua pelo nome do seu banco de dados
            user= os.getenv("USER"),      # Substitua pelo seu nome de usuário
            password= os.getenv("PASSWORD"),    # Substitua pela sua senha
            host= os.getenv("HOST"),  # Endereço IPv6 do servidor PostgreSQL (Radmin VPN)
            port= os.getenv("PORT")            
        )
    
    def get_clientes(self):
        cursor = self.servidor.cursor(cursor_factory=DictCursor)
        cursor.execute("SELECT * FROM clientes WHERE nome = %s", (self.nome,))
        resultado = cursor.fetchall()

        if resultado:
            for row in resultado:
                return dict(row)

    def get_imoveis(self, tipo):
        cursor = self.servidor.cursor(cursor_factory=DictCursor)
        if tipo == 'Logradouro':
            cursor.execute("SELECT * FROM imoveis WHERE logradouro = %s", (self.nome,))
        else:
            cursor.execute("SELECT * FROM imoveis WHERE referencia = %s", (self.nome,))
        resultado = cursor.fetchall()

        if resultado:
            for row in resultado:
                return dict(row)

    def get_corretores(self):
        cursor = self.servidor.cursor(cursor_factory=DictCursor)
        cursor.execute("SELECT * FROM corretor WHERE nome = %s", (self.nome,))
        resultado = cursor.fetchall()
        if resultado:
            for row in resultado:
                return dict(row)