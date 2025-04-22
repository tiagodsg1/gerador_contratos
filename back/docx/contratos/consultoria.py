from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt

from back.docx.src.retirar import retirar
from back.docx.src.retirar import delete_paragraph
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import remover_trecho
from back.docx.src.retirar import substituir_trecho_tabela
def consultoria(corretor, imovel, info_ad, caminho_documento, sucesso, error, download):
    try:
        documento = Document(caminho_documento)

        for table_index, tabela in enumerate(documento.tables):
            for row in tabela.rows:
                for cell in row.cells:
                    #Parte compradora
                    if '#PARTE_CONTRATANTE' in cell.text:
                        substituir_trecho_tabela(cell, '#PARTE_CONTRATANTE', info_ad['cliente0']['nome'])
                        
                    if '#NACIONALIDADE' in cell.text:
                        substituir_trecho_tabela(cell, '#NACIONALIDADE', 'Brasileiro(a)')

                    if '#ESTADO CIVIL' in cell.text:
                        if info_ad['cliente0']['estado_civil'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#ESTADO CIVIL', info_ad['cliente0']['estado_civil'])
                    
                    if '#CPF' in cell.text:
                        if info_ad['cliente0']['cpf_cnpj'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#CPF', info_ad['cliente0']['cpf_cnpj'])
                    
                    if '#E_MAIL' in cell.text:
                        if info_ad['cliente0']['email'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#E_MAIL', info_ad['cliente0']['email'])

                    
                    if '#ENDEREÇO' in cell.text:
                        if info_ad['cliente0']['logradouro'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        
                        else:
                            substituir_trecho_tabela(cell, '#ENDEREÇO', info_ad['cliente0']['logradouro'])

                    
                    if '#CEP' in cell.text:
                        if info_ad['cliente0']['cep'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#CEP', info_ad['cliente0']['cep'])
                    
                    if '#1PARTE_CONTRATANTE' in cell.text:
                        substituir_trecho_tabela(cell, '#1PARTE_CONTRATANTE', info_ad['cliente0']['nome'])

        #Parte Imobiliária
        for paragrafo in documento.paragraphs:
            texto = paragrafo.text
            if '#END_IMOVEL' in texto:
                substituir_texto(paragrafo, '#END_IMOVEL', f'{imovel["logradouro"]}, {imovel["numero"]}, {imovel["bairro"]}, {imovel["cidade"]}, {imovel["estado"]}')

            if '#3CEP' in texto:
                substituir_texto(paragrafo, '#3CEP', imovel['cep'])   

            if '#MINIMO_COMPRA' in texto:
                if info_ad['min_valor'] == None:
                    substituir_texto(paragrafo, '#MINIMO_COMPRA', imovel['valor'])
                else:
                    substituir_texto(paragrafo, '#MINIMO_COMPRA', info_ad['min_valor'])

            if '#VALOR_AVALIADO' in texto:
                if info_ad['av_valor'] == None:
                    substituir_texto(paragrafo, '#VALOR_AVALIADO', imovel['valor'])
                else:
                    substituir_texto(paragrafo, '#VALOR_AVALIADO', info_ad['av_valor'])

            if '#PROP_AUTORIZADA' in texto:
                substituir_texto(paragrafo, '#PROP_AUTORIZADA', info_ad['pro_valor'])
            
            if 'CONSULTORIA_R$' in texto:
                substituir_texto(paragrafo, '#CONSULTORIA_R$', info_ad['cons_valor'])

            if '#FORO' in texto:
                substituir_texto(paragrafo, '#FORO', imovel['cidade'])
        
        download.emit(documento)
    except Exception as e:
        error.emit(str(e))              


