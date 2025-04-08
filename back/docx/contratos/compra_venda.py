from docx import Document

from back.docx.src.inserir_tabelas import inserir_tabelas
from back.docx.src.retirar import retirar
from back.docx.src.retirar import delete_paragraph
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import remover_trecho
from back.docx.src.retirar import substituir_trecho_tabela
def compra_venda(caminho_documento, dados_comprador, dados_vendedor, dados_imovel, dados_corretor, dados_cliente2, dados_cliente3, info_ad, sucesso, error, download):
    try:
        documento = Document(caminho_documento)
        inserir_tabelas(documento, documento.tables[0], dados_cliente2, dados_cliente3)
        retirar(documento)
        for table_index, tabela in enumerate(documento.tables):
            for row in tabela.rows:
                for celula in row.cells:
                    #Parte vendedora
                    if "#PARTE_VENDEDORA" in celula.text:
                        substituir_trecho_tabela(celula, "#PARTE_VENDEDORA", dados_vendedor['nome'])

                    if '#NACIONALIDADE' in celula.text:
                        if dados_vendedor['nacionalidade'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, '#NACIONALIDADE', dados_vendedor['nacionalidade'])
                    
                    if '#ESTADO CIVIL' in celula.text:
                        if dados_vendedor['estado_civil'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, 'ESTADO CIVIL', dados_vendedor['estado_civil'])
                    
                    if '#CPF' in celula.text:
                        if dados_vendedor['cpf'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, 'CPF', dados_vendedor['cpf'])

                    if '#E_MAIL' in celula.text:
                        if dados_vendedor['email'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, 'E_MAIL', dados_vendedor['email'])

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
                            substituir_trecho_tabela(celula, 'ENDERECO', string_replace)
                    
                    if '#CEP' in celula.text:
                        if dados_vendedor['cep'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, 'CEP', dados_vendedor['cep'])

                    #Parte compradora

                    if '#PARTE_COMPRADORA' in celula.text:
                        substituir_trecho_tabela(celula, '#PARTE_COMPRADORA', dados_comprador['nome'])
                    
                    if '#2NACIONALIDADE' in celula.text:
                        if dados_comprador['nacionalidade'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, '#2NACIONALIDADE', dados_comprador['nacionalidade'])

                    if '#2ESTADO CIVIL' in celula.text:
                        if dados_comprador['estado_civil'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, '#2ESTADO CIVIL', dados_comprador['estado_civil'])
                        
                    if '#2CPF' in celula.text:
                        if dados_comprador['cpf'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, '#2CPF', dados_comprador['cpf'])
                    
                    if '#2E_MAIL' in celula.text:
                        if dados_comprador['email'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        
                        else:
                            substituir_trecho_tabela(celula, '#2E_MAIL', dados_comprador['email'])
                    
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
                            substituir_trecho_tabela(celula, '2ENDERECO', string_replace)

                    if '#2CEP' in celula.text:
                        if dados_comprador['cep'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, '#2CEP', dados_comprador['cep'])

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
                            substituir_trecho_tabela(celula, '#END_IMOVEL', string_replace)

                    if '#3CEP' in celula.text:
                        if dados_imovel['cep'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)

                        else:
                            substituir_trecho_tabela(celula, '#3CEP', dados_imovel['cep'])

                    if '#CARTORIO' in celula.text:
                        if info_ad['cartorio'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, '#CARTORIO', info_ad['cartorio'])
                    
                    if '#MATRICULA' in celula.text:
                        if info_ad['matricula'] == '':
                            if dados_imovel['matricula'] == None:
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#MATRICULA', dados_imovel['matricula'])
                        else:
                            substituir_trecho_tabela(celula, '#MATRICULA', info_ad['matricula'])

                    if '#INSCRICAO_IPTU' in celula.text:
                        if info_ad['n_iptu'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, '#INSCRICAO_IPTU', info_ad['n_iptu'])
        for paragrafo in documento.paragraphs:
            retirar(paragrafo)
            texto = paragrafo.text
            if '#SINAL' in texto:
                if info_ad['subsidio'] == '':
                    delete_paragraph(paragrafo)
                else:
                    substituir_texto(paragrafo, '#SINAL', info_ad['subsidio'])

            if '#ENTRADA' in texto:
                if info_ad['entrada'] == '':
                    delete_paragraph(paragrafo)
                else:
                    substituir_texto(paragrafo, '#ENTRADA', info_ad['entrada'])

            if '#FINANCIAMENTO' in texto:
                if info_ad['financiamento'] == '':
                    delete_paragraph(paragrafo)
                else:
                    substituir_texto(paragrafo, '#FINANCIAMENTO', info_ad['financiamento'])

            if '#FGTS' in texto:
                if info_ad['fgts'] == '':
                    delete_paragraph(paragrafo)
                else:
                    substituir_texto(paragrafo, '#FGTS', info_ad['fgts'])

            if '#SUBSIDIO' in texto:
                if info_ad['subsidio'] == '':
                    delete_paragraph(paragrafo)
                else:
                    substituir_texto(paragrafo, '#SUBSIDIO', info_ad['subsidio'])
    
            if 'PARÁGRAFO TERCEIRO: A PARTE VENDEDORA ' in texto:
                if info_ad['isencao'] == '':
                    delete_paragraph(paragrafo)
                else:
                    substituir_texto(paragrafo, '#RETORNO', info_ad['isencao'])

            if 'A posse do imóvel será concedida à PARTE COMPRADORA no momento ' in texto:
                if info_ad['posse'] == '':
                    delete_paragraph(paragrafo)
                else:
                    substituir_texto(paragrafo, '#POSSE_OU_REGISTRO', info_ad['posse'])

            if 'Se a posse se der após a assinatura da escritura pública ou do contrato de financiamento,' in texto:
                if info_ad['escritura'] == True:
                    delete_paragraph(paragrafo)
            
            if '#CORRETOR' in texto:
                substituir_texto(paragrafo, '#CORRETOR', dados_corretor['nome'])

            if '#FORO_CIDADE' in texto:
                substituir_texto(paragrafo, '#FORO_CIDADE', dados_imovel['cidade'])    

        download.emit(documento)
    
    except Exception as e:
        error.emit(str(e))
                    

