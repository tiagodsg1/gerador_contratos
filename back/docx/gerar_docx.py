from back.docx.contratos.admin_locacao import administracao_locacao
from back.docx.contratos.auto_venda import auto_venda
from back.docx.contratos.compra_venda import compra_venda
from back.docx.contratos.locacao import locacao
from back.docx.contratos.recibo_pagamento import recibo_pagamento
from back.docx.contratos.consultoria import consultoria

class GerarDocx:
    def __init__(self, t_contrato, caminho_documento, dicionario):
        
        self.caminho_documento = caminho_documento
        self.t_contrato = t_contrato

        if self.t_contrato == 'Administração de Locação':
            self.dados_corretor = dicionario['corretor']
            self.dados_imovel = dicionario['imovel']
            self.info_ad = dicionario['info_ad']
            self.sucesso = dicionario['sucesso']
            self.error = dicionario['error']
            self.download = dicionario['download']
            administracao_locacao(self.dados_corretor, self.dados_imovel, self.info_ad, self.caminho_documento, self.sucesso, self.error, self.download)

        if self.t_contrato == 'Autorização de Venda':

            self.dados_corretor = dicionario['corretor']
            self.dados_imovel = dicionario['imovel']
            self.info_ad = dicionario['info_ad']
            self.sucesso = dicionario['sucesso']
            self.error = dicionario['error']
            self.download = dicionario['download']
            auto_venda(self.caminho_documento, self.dados_corretor, self.dados_imovel, self.info_ad, self.sucesso, self.error, self.download)
                        
        if self.t_contrato == 'Compromisso de Compra e Venda':
            self.dados_imovel = dicionario['imovel']
            self.dados_corretor = dicionario['corretor']
            self.info_ad = dicionario['info_ad']
            self.sucesso = dicionario['sucesso']
            self.error = dicionario['error']
            self.download = dicionario['download']
            compra_venda(self.caminho_documento, self.dados_imovel, self.dados_corretor, self.info_ad, self.sucesso, self.error, self.download)
            
        if self.t_contrato == 'Recibo de Pagamento':
            self.dados_corretor = dicionario['corretor']
            self.info_ad = dicionario['info_ad']
            self.sucesso = dicionario['sucesso']
            self.error = dicionario['error']
            self.download = dicionario['download']
            recibo_pagamento(self.dados_corretor, self.info_ad, self.caminho_documento, self.sucesso, self.error, self.download)

        if self.t_contrato == 'Consultoria':
            self.dados_cliente = dicionario['cliente']
            self.dados_corretor = dicionario['corretor']
            self.dados_imovel = dicionario['imovel']
            self.min_valor = dicionario['min_valor']
            self.av_valor = dicionario['av_valor']
            self.pro_valor = dicionario['pro_valor']
            self.cons_valor = dicionario['cons_valor']
            self.sucesso = dicionario['sucesso']
            self.error = dicionario['error']
            self.download = dicionario['download']
            consultoria(self.dados_cliente, self.dados_corretor, self.dados_imovel, self.min_valor, self.av_valor, self.pro_valor, self.cons_valor, self.caminho_documento, self.sucesso, self.error, self.download)
        
        if self.t_contrato == 'Locação':
            self.dados_corretor = dicionario['corretor']
            self.dados_imovel = dicionario['imovel']
            self.info_ad = dicionario['info_ad']
            self.sucesso = dicionario['sucesso']
            self.error = dicionario['error']
            self.download = dicionario['download']
            locacao(self.dados_corretor, self.dados_imovel, self.caminho_documento, self.info_ad, self.sucesso, self.error, self.download)
