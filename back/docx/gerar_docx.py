from back.docx.admin_locacao import administracao_locacao
from back.docx.auto_venda import auto_venda
#from back.docx.compra_venda import compra_venda
class GerarDocx:
    def __init__(self, t_contrato, caminho_documento, dicionario):
        
        self.caminho_documento = caminho_documento
        self.t_contrato = t_contrato

        self.cartorio = None
        self.iptu = None
        self.luz = None
        self.relogio = None
        self.monobitrifasico = None
        self.gas = None
        self.funesbom = None
    
        '''observacao = str(self.dados_imovel['observacao_privada'])
        extrair_dados = observacao.split(',')
        if len(extrair_dados) == 1:
            self.dados_privados = False
        else:
            for dado in extrair_dados:
                if 'Cartório' in dado:
                    self.cartorio = dado
                    
                if 'IPTU' in dado:
                    self.iptu = dado

                if 'Número Cliente Enel' in dado:
                    self.luz = dado

                if 'Número Relógio Enel' in dado:
                    self.relogio = dado

                if 'Sistema elétrico' in dado:
                    self.monobitrifasico = dado

                if 'Número Cliente Naturgy' in dado:
                    self.gas = dado

                if 'FUNESBOM' in dado:
                    self.funesbom = dado'''
        
        if self.t_contrato == 'Administração de Locação':
            self.dados_cliente = dicionario['cliente']
            self.dados_imovel = dicionario['imovel']
            self.dados_cliente2 = dicionario['cliente2']
            self.dados_cliente3 = dicionario['cliente3']
            self.sucesso = dicionario['sucesso']
            self.error = dicionario['error']
            self.percentual = dicionario['percentual'] 
            administracao_locacao(self.dados_cliente, self.dados_imovel, self.dados_cliente2, self.dados_cliente3, self.caminho_documento, self.sucesso, self.error, self.percentual, self.cartorio, self.iptu, self.luz, self.relogio, self.monobitrifasico, self.gas, self.funesbom)

        if self.t_contrato == 'Autorização de Venda':

            self.dados_cliente = dicionario['cliente']
            self.dados_corretor = dicionario['corretor']
            self.dados_imovel = dicionario['imovel']
            self.dados_cliente2 = dicionario['cliente2']
            self.dados_cliente3 = dicionario['cliente3']
            self.sucesso = dicionario['sucesso']
            self.error = dicionario['error']
            auto_venda(self.dados_cliente, self.dados_corretor, self.dados_imovel, self.dados_cliente2, self.dados_cliente3, self.sucesso, self.error, self.cartorio, self.iptu, self.luz, self.relogio, self.monobitrifasico, self.gas, self.funesbom)
                        
        '''if self.t_contrato == 'Compromisso de Compra e Venda':
            self.dados_comprador = dicionario['comprador']
            self.dados_vendedor = dicionario['vendedor']
            self.dados_imovel = dicionario['imovel']
            self.dados_corretor = dicionario['corretor']
            self.dados_cliente2 = dicionario['cliente2']
            self.dados_cliente3 = dicionario['cliente3']
            self.sucesso = dicionario['sucesso']
            self.error = dicionario['error']
            compra_venda(self.dados_comprador, self.dados_vendedor, self.dados_imovel, self.dados_corretor, self.dados_cliente2, self.dados_cliente3, self.sucesso, self.error, self.cartorio)'''
            
    