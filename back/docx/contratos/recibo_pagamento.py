from docx import Document

from back.docx.src.retirar import retirar
from back.docx.src.retirar import delete_paragraph
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import remover_trecho
from back.docx.src.retirar import substituir_trecho_tabela

def recibo_pagamento(corretor, pagador, recebedor, tipo_pag, mot_pag, quant_pag, caminho_documento, data_pag, sucesso, error, download):
    try:
        documento = Document(caminho_documento)
        retirar(documento)

        for paragrafo in documento.paragraphs:
            texto = paragrafo.text
            #Parte recebedora
            if '#PARTE_RECEBEDORA' in paragrafo.text:
                substituir_texto(paragrafo, '#PARTE_RECEBEDORA', recebedor['nome'])
            
            if recebedor['cpf_cnpj'] == 'None':
                if '#CPF' in paragrafo.text:
                    remover_trecho(paragrafo, ', CPF #CPF', '')
            else:
                if '#CPF' in paragrafo.text:
                    substituir_texto(paragrafo, '#CPF', recebedor['cpf_cnpj'])

            #Parte pagadora
            if '#PARTE_PAGADORA' in paragrafo.text:
                substituir_texto(paragrafo, '#PARTE_PAGADORA', pagador['nome'])

            if pagador['cpf_cnpj'] == 'None':
                if '#2_CPF' in paragrafo.text:
                    remover_trecho(paragrafo, ', CPF #2_CPF', '')

            else:
                if '#2_CPF' in paragrafo.text:
                    substituir_texto(paragrafo, '#2_CPF', pagador['cpf_cnpj'])

            #Dados do pagamento
            if '#MOTIVO_PAGAMENTO' in paragrafo.text:
                    substituir_texto(paragrafo, '#MOTIVO_PAGAMENTO', mot_pag)

            if '#QUANTIA' in paragrafo.text:
                substituir_texto(paragrafo, '#QUANTIA', quant_pag)

            
            if tipo_pag == None:
                if 'a favor da HouseUp,' in paragrafo.text:
                    remover_trecho(paragrafo, ', a favor da HouseUp, CNPJ 47.952.730/0001-56', '')
                
                if 'por transferência bancária' in paragrafo.text:
                    remover_trecho(paragrafo, 'por transferência bancária', '')

            else:
                if 'por transferência bancária' in paragrafo.text:
                    substituir_texto(paragrafo, 'por transferência bancária', f'por {tipo_pag}')

            #Inserir data
            if '#DATA_TRANSFERENCIA' in paragrafo.text:
                substituir_texto(paragrafo, '#DATA_TRANSFERENCIA', data_pag)
    
        download.emit(documento)
    except Exception as e:
        error(e)



            
            

