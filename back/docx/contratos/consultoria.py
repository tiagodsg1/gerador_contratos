from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from back.docx.src.save_document import save_document

def consultoria(cliente, corretor, imovel, min_valor, av_valor, pro_valor, cons_valor, caminho_documento, sucesso, error):
    try:
        documento = Document(caminho_documento)

        for table_index, tabela in enumerate(documento.tables):
            for row in tabela.rows:
                for cell in row.cells:
                    #Parte compradora
                    if '#PARTE_CONTRATANTE' in cell.text:
                        cell.text = cell.text.replace('#PARTE_CONTRATANTE', cliente['nome'])
                        
                    if '#NACIONALIDADE' in cell.text:
                        cell.text = cell.text.replace('#NACIONALIDADE', 'Brasileiro(a)')

                    if '#ESTADO CIVIL' in cell.text:
                        if cliente['estado_civil'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#ESTADO CIVIL', cliente['estado_civil'])
                    
                    if '#CPF' in cell.text:
                        if cliente['cpf_cnpj'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#CPF', cliente['cpf_cnpj'])
                    
                    if '#E_MAIL' in cell.text:
                        if cliente['email'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#E_MAIL', cliente['email'])

                    
                    if '#ENDEREÇO' in cell.text:
                        if cliente['logradouro'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        
                        else:
                            cell.text = cell.text.replace('#ENDEREÇO', cliente['logradouro'])

                    
                    if '#CEP' in cell.text:
                        if cliente['cep'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#CEP', cliente['cep'])
                    
                    if '#1PARTE_CONTRATANTE' in cell.text:
                        cell.text = cell.text.replace('#1PARTE_CONTRATANTE', cliente['nome'])
                        for paragrafo in cell.paragraphs:
                            if cell.text in paragrafo.text:
                                paragrafo.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                                paragrafo.style.font.name = 'Times New Roman'
                                paragrafo.style.font.size = Pt(12)
                                
                                
                                

        #Parte Imobiliária
        for paragrafo in documento.paragraphs:
            if '#END_IMOVEL' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#END_IMOVEL', f'{imovel["logradouro"]}, {imovel["numero"]}, {imovel["bairro"]}, {imovel["cidade"]}, {imovel["estado"]}')

            if '#3CEP' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#3CEP', imovel['cep'])   

            if '#MINIMO_COMPRA' in paragrafo.text:
                if min_valor == None:
                    paragrafo.text = paragrafo.text.replace('#MINIMO_COMPRA', imovel['valor'])
                else:
                    paragrafo.text = paragrafo.text.replace('#MINIMO_COMPRA', min_valor)

            if '#VALOR_AVALIADO' in paragrafo.text:
                if av_valor == None:
                    paragrafo.text = paragrafo.text.replace('#VALOR_AVALIADO', imovel['valor'])
                else:
                    paragrafo.text = paragrafo.text.replace('#VALOR_AVALIADO', av_valor)

            if '#PROP_AUTORIZADO' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#PROP_AUTORIZADO', pro_valor)
            
            if 'CONSULTORIA_R$' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('CONSULTORIA_R$', cons_valor)

            if '#FORO' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#FORO', imovel['cidade'])
        
        file_name = save_document()
        documento.save(file_name)
        sucesso.emit("Contrato gerado com sucesso!")
    except Exception as e:
        error.emit(str(e))              


