import psycopg2
import os

from back.bd.verif import get_env_path
from dotenv import load_dotenv

class LogCorretor:
    def __init__(self, nome_corretor, id_corretor, creci, tipo, contrato, 
                 data_de_lancamento, imovel, bairro_imovel, cidade_imovel, 
                 id_imovel, cliente_contratante, bairro_cliente, cidade_cliente, id_cliente):
        self.nome_corretor = nome_corretor
        self.id_corretor = id_corretor
        self.creci = creci
        self.tipo = tipo
        self.contrato = contrato
        self.data_de_lancamento = data_de_lancamento
        self.imovel = imovel
        self.bairro_imovel = bairro_imovel
        self.cidade_imovel = cidade_imovel
        self.id_imovel = id_imovel
        self.cliente_contratante = cliente_contratante
        self.bairro_cliente = bairro_cliente
        self.cidade_cliente = cidade_cliente
        self.id_cliente = id_cliente

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