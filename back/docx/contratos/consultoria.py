from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt

from back.docx.src.retirar import retirar
from back.docx.src.retirar import delete_paragraph
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import remover_trecho
from back.docx.src.retirar import substituir_trecho_tabela
def consultoria(cliente, corretor, imovel, min_valor, av_valor, pro_valor, cons_valor, caminho_documento, sucesso, error, download):
    try:
        documento = Document(caminho_documento)
        retirar(documento)

        for table_index, tabela in enumerate(documento.tables):
            for row in tabela.rows:
                for cell in row.cells:
                    #Parte compradora
                    if '#PARTE_CONTRATANTE' in cell.text:
                        substituir_trecho_tabela(cell, '#PARTE_CONTRATANTE', cliente['nome'])
                        
                    if '#NACIONALIDADE' in cell.text:
                        substituir_trecho_tabela(cell, '#NACIONALIDADE', 'Brasileiro(a)')

                    if '#ESTADO CIVIL' in cell.text:
                        if cliente['estado_civil'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#ESTADO CIVIL', cliente['estado_civil'])
                    
                    if '#CPF' in cell.text:
                        if cliente['cpf_cnpj'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#CPF', cliente['cpf_cnpj'])
                    
                    if '#E_MAIL' in cell.text:
                        if cliente['email'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#E_MAIL', cliente['email'])

                    
                    if '#ENDEREÇO' in cell.text:
                        if cliente['logradouro'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        
                        else:
                            substituir_trecho_tabela(cell, '#ENDEREÇO', cliente['logradouro'])

                    
                    if '#CEP' in cell.text:
                        if cliente['cep'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#CEP', cliente['cep'])
                    
                    if '#1PARTE_CONTRATANTE' in cell.text:
                        substituir_trecho_tabela(cell, '#1PARTE_CONTRATANTE', cliente['nome'])

        #Parte Imobiliária
        for paragrafo in documento.paragraphs:
            texto = paragrafo.text
            if '#END_IMOVEL' in texto:
                substituir_texto('#END_IMOVEL', f'{imovel["logradouro"]}, {imovel["numero"]}, {imovel["bairro"]}, {imovel["cidade"]}, {imovel["estado"]}')

            if '#3CEP' in texto:
                substituir_texto('#3CEP', imovel['cep'])   

            if '#MINIMO_COMPRA' in texto:
                if min_valor == None:
                    substituir_texto('#MINIMO_COMPRA', imovel['valor'])
                else:
                    substituir_texto('#MINIMO_COMPRA', min_valor)

            if '#VALOR_AVALIADO' in texto:
                if av_valor == None:
                    substituir_texto('#VALOR_AVALIADO', imovel['valor'])
                else:
                    substituir_texto('#VALOR_AVALIADO', av_valor)

            if '#PROP_AUTORIZADO' in texto:
                substituir_texto('#PROP_AUTORIZADO', pro_valor)
            
            if 'CONSULTORIA_R$' in texto:
                substituir_texto('CONSULTORIA_R$', cons_valor)

            if '#FORO' in texto:
                substituir_texto('#FORO', imovel['cidade'])
        
        download.emit(documento)
    except Exception as e:
        error.emit(str(e))              


