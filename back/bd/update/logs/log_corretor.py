import psycopg2
import os

from back.bd.verif import get_env_path
from dotenv import load_dotenv

class LogCorretor:
    def __init__(self):
        super().__init__()

        self.bd = get_env_path()
        load_dotenv(self.bd)
        self.servidor = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST"),
            port=os.getenv("PORT")
        )

        self.cursor = self.servidor.cursor()

    def insert_logs(self, lista):
        self.nome_corretor = lista[0]
        self.id_corretor = lista[1]
        self.creci = lista[2]
        self.tipo = lista[3]
        self.contrato = lista[4]
        self.data_de_lancamento = lista[5]
        self.imovel = lista[6]
        self.bairro_imovel = lista[7]
        self.cidade_imovel = lista[8]
        self.id_imovel = lista[9]
        self.cliente_contratante = lista[10]
        self.bairro_cliente = lista[11]
        self.cidade_cliente = lista[12]
        self.id_cliente = lista[13]

        self.cursor.execute("""
        INSERT INTO log_corretor (
            nome_corretor, id_corretor, creci, tipo, contrato, data_de_lançamento,
            imovel, bairro_imovel, cidade_imovel, id_imovel, cliente_contratante, bairro_cliente,
            cidade_cliente, id_cliente
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
        self.nome_corretor, self.id_corretor, self.creci, self.tipo, self.contrato,
        self.data_de_lancamento, self.imovel, self.bairro_imovel, self.cidade_imovel, 
        self.id_imovel, self.cliente_contratante, self.bairro_cliente, self.cidade_cliente, 
        self.id_cliente ))
        
        self.servidor.commit()
        self.cursor.close()
        self.servidor.close()

    def get_logs(self, corretor):
        self.cursor.execute("""
        SELECT * FROM log_corretor WHERE nome_corretor = %s
        """, (corretor,))
        logs = self.cursor.fetchall()
        self.servidor.commit()
        self.cursor.close()
        self.servidor.close()
        return logs

