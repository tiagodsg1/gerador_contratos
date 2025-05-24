from playwright.sync_api import sync_playwright
import os, psycopg2, openpyxl, sys
from dotenv import load_dotenv
import time

from back.bd.update.update import Update_Dados
from back.bd.update.delete import Delete
from back.bd.verif import get_env_path

class Dados:
    def __init__(self, sucesso, error, finished, caminho_table, show_download, download_value, download_label):
        super().__init__()
        self.sucesso = sucesso  
        self.error = error
        self.finished = finished
        self.caminho_table = caminho_table
        self.show_download = show_download
        self.download_value = download_value
        self.download_label = download_label
        self.index = 0
        self.bd = get_env_path()
        load_dotenv(self.bd)

        try:
            self.servidor = psycopg2.connect(
                dbname= os.getenv("DB_NAME"),  # Substitua pelo nome do seu banco de dados
                user= os.getenv("USER"),      # Substitua pelo seu nome de usuário
                password= os.getenv("PASSWORD"),    # Substitua pela sua senha
                host= os.getenv("HOST"),  # Endereço IPv6 do servidor PostgreSQL (Radmin VPN)
                port= os.getenv("PORT")             
            )
        except Exception as e:
            self.error.emit(f'Erro ao conectar com o banco de dados: {e}')
            sys.exit()
        
        self.download_table()

        '''except Exception as e:
            self.error.emit(f'Erro ao fazer o download{e}')
            self.servidor.close()'''

    def download_table(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            while page.locator('xpath=//*[@id="email"]'):
                page.wait_for_timeout(5000)
                try:
                    page.goto('https://app.tecimob.com.br/')
                    page.type('xpath=//*[@id="email"]', 'tiagodsg72@gmail.com')
                    break
                except:
                    pass

            page.type('xpath=//*[@id="password"]', '@imoveiscaixa2024')
            page.wait_for_timeout(5000)
            page.click('xpath=//*[@id="root"]/div/div/div[2]/div/form/button')
            page.wait_for_timeout(6000)
            page.goto("https://app.tecimob.com.br/config/bkp/show")
            page.wait_for_timeout(3000)
            page.click('xpath=//*[@id="root"]/div/div/main/div/div/div/div/div/div[1]/button')
            page.wait_for_timeout(5000)
            while page.locator('xpath=//*[@id="root"]/div/div[2]/main/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]/button/text()'):
                page.wait_for_timeout(5000)
                try:
                    if page.locator('xpath=//*[@id="root"]/div/div/main/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]/a').get_attribute('href'):
                        page.wait_for_timeout(3000)
                        break
                except:
                    page.reload()
            with page.expect_download() as download_info:
                page.click('xpath=//*[@id="root"]/div/div/main/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[3]/a')
            download = download_info.value
            arquivos = os.listdir(self.caminho_table)
            for arquivo in arquivos:
                os.remove(f'{self.caminho_table}/{arquivo}')
            download.save_as(f'{self.caminho_table}/tabela_old.xlsx')
            browser.close()
            self.extrair_nomes_bd()

    def extrair_nomes_bd(self):
        self.show_download.emit()
        self.download_label.emit('Extraindo dados do banco de dados...')
        for i in range(25):
            self.download_value.emit(self.index)
            self.index += 1
            time.sleep(0.1)
        cursor = self.servidor.cursor()
        cursor.execute("SELECT nome FROM Clientes")
        self.nomes = [nome[0] for nome in cursor.fetchall()]
        cursor.execute("SELECT referencia FROM Imoveis")
        self.referencias = [referencia[0] for referencia in cursor.fetchall()]
        cursor.close()
        self.extrair_nomes_planilha()
    
    def extrair_nomes_planilha(self):
        self.download_label.emit('Extraindo dados da planilha...')
        self.caminho = os.path.join(self.caminho_table, 'tabela_old.xlsx')
        planilha = openpyxl.load_workbook(self.caminho)
        aba = planilha['Clientes']
        self.nomes_planilha = [aba[f"D{i}"].value for i in range(2, aba.max_row+1)]

        aba_2 = planilha['Imóveis']
        self.referencias_planilha = [aba_2[f"B{i}"].value for i in range(2, aba_2.max_row+1)]
        planilha.close()
        for i in range(25):
            self.download_value.emit(self.index)
            self.index += 1
            time.sleep(0.1)
        self.comparar_dados()
        
    def comparar_dados(self):
        self.download_label.emit('Comparando dados...')
        lista_incluir_nomes = []
        for nome in self.nomes_planilha:
            if nome not in self.nomes:
                if '\xa0' in nome:
                    nome = nome.replace('\xa0', ' ')
                lista_incluir_nomes.append(nome)
                
        lista_excluir_nomes = []
        for nome in self.nomes:
            if nome not in self.nomes_planilha:
                lista_excluir_nomes.append(nome)

        lista_incluir_imoveis = []
        for referencia in self.referencias_planilha:
            if referencia not in self.referencias:
                if referencia not in lista_incluir_imoveis:
                    lista_incluir_imoveis.append(referencia)

        lista_excluir_imoveis = []
        for referencia in self.referencias:
            if referencia not in self.referencias_planilha:
                lista_excluir_imoveis.append(referencia)
        try:
            self.download_label.emit('Excluindo clientes...')
            Delete(lista_excluir_nomes, lista_excluir_imoveis)
            self.download_label.emit('Atualizando clientes...')
            Update_Dados(lista_incluir_nomes, lista_incluir_imoveis, self.caminho, self.download_label, self.download_value, self.index)
            for i in range(25):
                self.download_value.emit(self.index)
                self.index += 1
                time.sleep(0.1)
            self.sucesso.emit('Dados atualizados com sucesso.')
        except Exception as e:
            self.error.emit('Erro ao atualizar os dados.\n' + str(e))
        self.servidor.close()
        self.finished.emit()