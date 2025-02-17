import psycopg2
from psycopg2.extras import DictCursor

class GetDados():
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.servidor = psycopg2.connect(
            dbname="houseup",  
            user="postgres",      
            password="houseuptec",    
            host="fdfd::1acd:4580",  
            port="5432"              
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