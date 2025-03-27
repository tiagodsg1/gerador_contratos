from docx import Document
from back.docx.src.save_document import save_document

def recibo_pagamento(corretor, pagador, recebedor, tipo_pag, mot_pag, quant_pag, caminho_documento, data_pag, sucesso, error):
    try:
        documento = Document(caminho_documento)

        for paragrafo in documento.paragraphs:
            #Parte recebedora
            if '#PARTE_RECEBEDORA' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#PARTE_RECEBEDORA', recebedor['nome'])
            
            if recebedor['cpf_cnpj'] == 'None':
                if '#CPF' in paragrafo.text:
                    paragrafo.text = paragrafo.text.replace(', CPF #CPF', '')
            else:
                if '#CPF' in paragrafo.text:
                    paragrafo.text = paragrafo.text.replace('#CPF', recebedor['cpf_cnpj'])

            #Parte pagadora
            if '#PARTE_PAGADORA' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#PARTE_PAGADORA', pagador['nome'])

            if pagador['cpf_cnpj'] == 'None':
                if '#2_CPF' in paragrafo.text:
                    paragrafo.text = paragrafo.text.replace(', CPF #2_CPF', '')

            else:
                if '#2_CPF' in paragrafo.text:
                    paragrafo.text = paragrafo.text.replace('#2_CPF', pagador['cpf_cnpj'])

            #Dados do pagamento
            if '#MOTIVO_PAGAMENTO' in paragrafo.text:
                    paragrafo.text = paragrafo.text.replace('#MOTIVO_PAGAMENTO', mot_pag)

            if '#QUANTIA' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#QUANTIA', quant_pag)

            
            if tipo_pag == None:
                if 'a favor da HouseUp,' in paragrafo.text:
                    paragrafo.text = paragrafo.text.replace(', a favor da HouseUp, CNPJ 47.952.730/0001-56', '')
                
                if 'por transferência bancária' in paragrafo.text:
                    paragrafo.text = paragrafo.text.replace('por transferência bancária', '')

            else:
                if 'por transferência bancária' in paragrafo.text:
                    paragrafo.text = paragrafo.text.replace('por transferência bancária', f'por {tipo_pag}')

            #Inserir data
            if '#DATA_TRANSFERENCIA' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#DATA_TRANSFERENCIA', data_pag)
    
        file_name = save_document()
        documento.save(file_name)
        sucesso.emit("Contrato gerado com sucesso!")
    except Exception as e:
        error(e)



            
            

