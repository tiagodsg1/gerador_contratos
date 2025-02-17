from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt

from back.docx.inserir_tabelas import inserir_tabelas


def compra_venda(dados_comprador, dados_vendedor, dados_imovel, dados_corretor, dados_cliente2, dados_cliente3, sucesso, error, cartorio):
   try:
        documento = Document('./Contratos/Compromisso de Compra e Venda.docx')
        inserir_tabelas(documento, documento.tables[0], dados_cliente2, dados_cliente3)

        for table_index, tabela in enumerate(documento.tables):
            for row in tabela.rows:
                for celula in row.cells:
                    #Parte vendedora
                    if "#PARTE_VENDEDORA" in celula.text:
                        celula.text = celula.text.replace("#PARTE_VENDEDORA", dados_vendedor['nome'])

                    if '#NACIONALIDADE' in celula.text:
                        if dados_vendedor['nacionalidade'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            celula.text = celula.text.replace('#NACIONALIDADE', dados_vendedor['nacionalidade'])
                    
                    if '#ESTADO CIVIL' in celula.text:
                        if dados_vendedor['estado_civil'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            celula.text = celula.text.replace('ESTADO CIVIL', dados_vendedor['estado_civil'])
                    
                    if '#CPF' in celula.text:
                        if dados_vendedor['cpf'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            celula.text = celula.text.replace('CPF', dados_vendedor['cpf'])

                    if '#E_MAIL' in celula.text:
                        if dados_vendedor['email'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            celula.text = celula.text.replace('E_MAIL', dados_vendedor['email'])

                    if '#ENDERECO' in celula.text:
                        if dados_vendedor['logradouro'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            lista_itens = ['logradouro', 'numero', 'bairro', 'cidade', 'estado']
                            string_replace = ''
                            for i in range(1,5):
                                if dados_vendedor[lista_itens[i]] == None:
                                    pass
                                else:
                                    if lista_itens[i] == 'estado':
                                        string_replace += dados_vendedor[lista_itens[i]]
                                    else:
                                        string_replace += dados_vendedor[lista_itens[i]] + ','
                            celula.text = celula.text.replace('ENDERECO', string_replace)
                    
                    if '#CEP' in celula.text:
                        if dados_vendedor['cep'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            celula.text = celula.text.replace('CEP', dados_vendedor['cep'])

                    #Parte compradora

                    if '#PARTE_COMPRADORA' in celula.text:
                        celula.text = celula.text.replace('#PARTE_COMPRADORA', dados_comprador['nome'])
                    
                    if '#2NACIONALIDADE' in celula.text:
                        if dados_comprador['nacionalidade'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            celula.text = celula.text.replace('#2NACIONALIDADE', dados_comprador['nacionalidade'])

                    if '#2ESTADO CIVIL' in celula.text:
                        if dados_comprador['estado_civil'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            celula.text = celula.text.replace('#2ESTADO CIVIL', dados_comprador['estado_civil'])
                        
                    if '#2CPF' in celula.text:
                        if dados_comprador['cpf'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            celula.text = celula.text.replace('#2CPF', dados_comprador['cpf'])
                    
                    if '#2E_MAIL' in celula.text:
                        if dados_comprador['email'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        
                        else:
                            celula.text = celula.text.replace('#2E_MAIL', dados_comprador['email'])
                    
                    if '2ENDERECO' in celula.text:
                        if dados_comprador['logradouro'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            lista_itens = ['logradouro', 'numero', 'bairro', 'cidade', 'estado']
                            string_replace = ''
                            for i in range(1,5):
                                if dados_comprador[lista_itens[i]] == None:
                                    pass
                                else:
                                    if lista_itens[i] == 'estado':
                                        string_replace += dados_comprador[lista_itens[i]]
                                    else:
                                        string_replace += dados_comprador[lista_itens[i]] + ','
                            celula.text = celula.text.replace('2ENDERECO', string_replace)

                    if '#2CEP' in celula.text:
                        if dados_comprador['cep'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            celula.text = celula.text.replace('#2CEP', dados_comprador['cep'])

                    if '#END_IMOVEL' in celula.text:
                        if dados_imovel['logradouro'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            lista_itens = ['logradouro', 'numero', 'bairro', 'cidade', 'estado']
                            string_replace = ''
                            for i in range(1,5):
                                if dados_imovel[lista_itens[i]] == None:
                                    pass
                                else:
                                    if lista_itens[i] == 'estado':
                                        string_replace += dados_imovel[lista_itens[i]]
                                    else:
                                        string_replace += dados_imovel[lista_itens[i]] + ','
                            celula.text = celula.text.replace('#END_IMOVEL', string_replace)

                    if '#3CEP' in celula.text:
                        if dados_imovel['cep'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)

                        else:
                            celula.text = celula.text.replace('#3CEP', dados_imovel['cep'])
                    
                    

