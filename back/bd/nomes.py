import psycopg2 
from dotenv import load_dotenv
import os

class GetNomes():
    def __init__(self):
        super().__init__()
        load_dotenv()
        self.servidor = psycopg2.connect(
            dbname= os.getenv("DB_NAME"),  # Substitua pelo nome do seu banco de dados
            user= os.getenv("USER"),      # Substitua pelo seu nome de usuário
            password= os.getenv("PASSWORD"),    # Substitua pela sua senha
            host= os.getenv("HOST"),  # Endereço IPv6 do servidor PostgreSQL (Radmin VPN)
            port= os.getenv("PORT")            
        )
        
    def get_clientes(self):
        cursor = self.servidor.cursor()
        cursor.execute("SELECT nome FROM clientes")
        return cursor.fetchall()
    
    def get_imoveis(self, tipo):
        if tipo == 'Logradouro':
            cursor = self.servidor.cursor()
            cursor.execute("SELECT logradouro FROM imoveis")
            logradouro = cursor.fetchall()

            cursor.execute("SELECT numero FROM imoveis")
            numero = cursor.fetchall()

            cursor.execute("SELECT id FROM imoveis")
            id = cursor.fetchall()

            lista_logradouro = []

            for i in range(len(logradouro)):
                item_logradouro = str(logradouro[i])
                item_logradouro = item_logradouro.replace("('", "").replace("',)", "")

                item_numero = str(numero[i])
                item_numero = item_numero.replace("('", "").replace("',)", "")

                item_id = str(id[i])
                item_id = item_id.replace("(", "").replace(",)", "")


                lista_logradouro.append(f'{item_logradouro}, {item_numero} - id {item_id}')
            return lista_logradouro
        
        else:
            cursor = self.servidor.cursor()
            cursor.execute("SELECT referencia FROM imoveis")
            return cursor.fetchall()
    

    def get_corretores(self):
        cursor = self.servidor.cursor()
        cursor.execute("SELECT nome FROM corretor")
        return cursor.fetchall()