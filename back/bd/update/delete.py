import psycopg2

class Delete:
    def __init__(self, nomes, imoveis):
        super().__init__()
        self.servidor = psycopg2.connect(
            dbname="houseup",
            user="postgres",      
            password="houseuptec",    
            host="fdfd::1acd:4580",  
            port="5432"              
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