import psycopg2
from dotenv import load_dotenv
import os
class Delete:
    def __init__(self, nomes, imoveis):
        super().__init__()
        load_dotenv()
        self.servidor = psycopg2.connect(
            dbname= os.getenv("DB_NAME"),  # Substitua pelo nome do seu banco de dados
            user= os.getenv("USER"),      # Substitua pelo seu nome de usuário
            password= os.getenv("PASSWORD"),    # Substitua pela sua senha
            host= os.getenv("HOST"),  # Endereço IPv6 do servidor PostgreSQL (Radmin VPN)
            port= os.getenv("PORT")            
        )
        self.nomes = nomes
        self.imoveis = imoveis
        self.deletar_dados_clientes()

    def deletar_dados_clientes(self):
        cursor = self.servidor.cursor()
        for nome in self.nomes:
            cursor.execute(f"DELETE FROM Clientes WHERE nome = '{nome}'")
        self.servidor.commit()
        cursor.close()

    def deletar_dados_imovel(self):
        cursor = self.servidor.cursor()
        for referencia in self.imoveis:
            cursor.execute(f"DELETE FROM Imoveis WHERE referencia = '{referencia}'")
        self.servidor.commit()
        cursor.close()