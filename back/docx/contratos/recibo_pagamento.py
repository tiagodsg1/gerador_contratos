from docx import Document

from back.docx.src.retirar import retirar
from back.docx.src.retirar import delete_paragraph
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import remover_trecho
from back.docx.src.retirar import substituir_trecho_tabela

def recibo_pagamento(corretor, info_ad, caminho_documento, sucesso, error, download):
    try:
        documento = Document(caminho_documento)

        for paragrafo in documento.paragraphs:
            texto = paragrafo.text
            #Parte recebedora
            if '#PARTE_RECEBEDORA' in texto:
                substituir_texto(paragrafo, '#PARTE_RECEBEDORA', info_ad['cliente0']['nome'])
            
            if info_ad['cliente0']['cpf_cnpj'] == 'None':
                if '#CPF' in texto:
                    remover_trecho(paragrafo, ', CPF #CPF', '')
            else:
                if '#CPF' in texto:
                    substituir_texto(paragrafo, '#CPF', info_ad['cliente0']['cpf_cnpj'])

            #Parte pagadora
            if '#PARTE_PAGADORA' in texto:
                substituir_texto(paragrafo, '#PARTE_PAGADORA', info_ad['cliente1']['nome'])

            if info_ad['cliente1']['cpf_cnpj'] == 'None':
                if '#2_CPF' in texto:
                    remover_trecho(paragrafo, ', CPF #2_CPF', '')

            else:
                if '#2_CPF' in texto:
                    substituir_texto(paragrafo, '#2_CPF', info_ad['cliente1']['cpf_cnpj'])

            #Dados do pagamento
            if '#MOTIVO_PAGAMENTO' in texto:
                    substituir_texto(paragrafo, '#MOTIVO_PAGAMENTO', info_ad['mot_pag'])

            if '#QUANTIA' in texto:
                substituir_texto(paragrafo, '#QUANTIA', 'R$ ' + info_ad['quant_pag'])

            
            if info_ad['tipo_pag'] == None:
                if 'a favor da HouseUp,' in texto:
                    remover_trecho(paragrafo, ', a favor da HouseUp, CNPJ 47.952.730/0001-56', '')
                
                if 'por transferência bancária' in texto:
                    remover_trecho(paragrafo, 'por transferência bancária', '')

            else:
                if 'por transferência bancária' in texto:
                    substituir_texto(paragrafo, 'por transferência bancária', f'por {info_ad['tipo_pag']}')

            #Inserir data
            if '#DATA_TRANSFERENCIA' in texto:
                substituir_texto(paragrafo, '#DATA_TRANSFERENCIA', info_ad['data_pag'])
    
        download.emit(documento)
    except Exception as e:
        error(e)



            
            

