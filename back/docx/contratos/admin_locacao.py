from docx import Document

from back.docx.src.inserir_tabelas import inserir_tabelas
from back.docx.src.retirar import retirar
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import remover_trecho
from back.docx.src.retirar import substituir_trecho_tabela
    
def administracao_locacao(dados_cliente, dados_imovel, dados_cliente2, dados_cliente3, info_ad, caminho_documento, sucesso, error, percentual, download):

    try:

        documento = Document(caminho_documento)
        porcentagem = int(percentual)

        inserir_tabelas(documento, documento.tables[0], dados_cliente2, dados_cliente3)
        retirar(documento)
            
        for tabela_index, tabela in enumerate(documento.tables):
            for linha in tabela.rows:
                for celula in linha.cells:
                    if dados_cliente:
                        #Parte do Cliente
                        if '#1PARTE_LOCADORA' == celula.text:
                            substituir_trecho_tabela(celula, '#1PARTE_LOCADORA', dados_cliente['nome'])

                        if '#PARTE_LOCADORA_ASSINATURA' in celula.text:
                            substituir_trecho_tabela(celula, '#PARTE_LOCADORA_ASSINATURA', dados_cliente['nome'])

                        if '#NACIONALIDADE' == celula.text:
                            substituir_trecho_tabela(celula, '#NACIONALIDADE', 'Brasileiro')

                        if '#ESTADO CIVIL' == celula.text:
                            if dados_cliente['estado_civil'] == None:
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)

                            else:
                                substituir_trecho_tabela(celula, '#ESTADO CIVIL', dados_cliente['estado_civil'])

                        if '#CPF' == celula.text:
                            if dados_cliente['cpf_cnpj'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#CPF', dados_cliente['cpf_cnpj'])

                        if '#E_MAIL' == celula.text:
                            if dados_cliente['email'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#E_MAIL', dados_cliente['email'])

                        if '#ENDERECO' == celula.text:
                            if dados_cliente['logradouro'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#ENDERECO', dados_cliente['logradouro'])

                        if '#1CEP' == celula.text:
                            if dados_cliente['cep'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#1CEP', dados_cliente['cep'])
                    
                    if dados_cliente2:
                        if '#2PARTE_CLIENTE' == celula.text:
                            substituir_trecho_tabela(celula, '#2PARTE_CLIENTE', dados_cliente2['nome'])

                        if '#2PARTE_CLIENTE_ASSINATURA' in celula.text:
                            substituir_trecho_tabela(celula, '#2PARTE_CLIENTE_ASSINATURA', dados_cliente2['nome'])
                        
                        if '#2NACIONALIDADE' == celula.text:
                            substituir_trecho_tabela(celula, '#2NACIONALIDADE', 'Brasileiro')

                        if '#2ESTADO CIVIL' == celula.text:
                            if dados_cliente2['estado_civil'] == None:
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#2ESTADO CIVIL', dados_cliente2['estado_civil'])

                        if '#2CPF' == celula.text:
                            if dados_cliente2['cpf_cnpj'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#2CPF', dados_cliente2['cpf_cnpj'])
                        
                        if '#2E_MAIL' == celula.text:
                            if dados_cliente2['email'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#2E_MAIL', dados_cliente2['email'])
                        
                        if '#2ENDERECO' == celula.text:
                            if dados_cliente2['logradouro'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#2ENDERECO', dados_cliente2['logradouro'])

                        if '#2CEP' == celula.text:
                            if dados_cliente2['cep'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#2CEP', dados_cliente2['cep'])
                        
                    if dados_cliente3:
                        if '#3PARTE_CLIENTE' == celula.text:
                            substituir_trecho_tabela(celula, '#3PARTE_CLIENTE', dados_cliente3['nome'])

                        if '#3PARTE_CLIENTE_ASSININATURA' in celula.text:
                            substituir_trecho_tabela(celula, '#3PARTE_CLIENTE_ASSININATURA', dados_cliente3['nome'])
                        
                        if '#3NACIONALIDADE' == celula.text:
                            substituir_trecho_tabela(celula, '#3NACIONALIDADE', 'Brasileiro')

                        if '#3ESTADO CIVIL' == celula.text:
                            if dados_cliente3['estado_civil'] == None:
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#3ESTADO CIVIL', dados_cliente3['estado_civil'])

                        if '#3CPF' == celula.text:
                            if dados_cliente3['cpf_cnpj'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#3CPF', dados_cliente3['cpf_cnpj'])
                        
                        if '#3E_MAIL' == celula.text:
                            if dados_cliente3['email'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#3E_MAIL', dados_cliente3['email'])
                        
                        if '#3ENDERECO' == celula.text:
                            if dados_cliente3['logradouro'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#3ENDERECO', dados_cliente3['logradouro'])

                        if '#3CEP' == celula.text:
                            if dados_cliente3['cep'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#3CEP', dados_cliente3['cep'])

                    if dados_imovel:
                        #Parte do Imóvel
                        if '#CARTORIO' == celula.text:
                            if info_ad['cartorio'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#CARTORIO', info_ad['cartorio'])

                        if '#MATRICULA' in celula.text:
                            if info_ad['matricula'] == '':
                                if dados_imovel['matricula'] == None:
                                    tabela_remove = documento.tables[tabela_index]
                                    remover_linha = tabela_remove.rows[linha._index]._element
                                    remover_linha.getparent().remove(remover_linha)
                                else:
                                    substituir_trecho_tabela(celula, '#MATRICULA', dados_imovel['matricula'])
                            else:
                                substituir_trecho_tabela(celula, '#MATRICULA', info_ad['matricula'])

                        if '#INSCRICAO_IPTU' == celula.text:
                            if info_ad['n_iptu'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#INSCRICAO_IPTU', info_ad['n_iptu'])        

                        if '#CONCESSIONARIA_LUZ' == celula.text:
                            if info_ad['luz'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#CONCESSIONARIA_LUZ', info_ad['luz'])
            
                        if '#RELOGIO' == celula.text:
                            if info_ad['relogio'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#RELOGIO', info_ad['relogio'])

                        if '#MONOBITRIFASICO' == celula.text:
                            if info_ad['monobitrifasico'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#MONOBITRIFASICO', info_ad['monobitrifasico'])

                        if '#CONCESSIONARIA_GAS' == celula.text:
                            if info_ad['gas']== '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#CONCESSIONARIA_GAS', info_ad['gas'])

                        if '#FUNESBOM' == celula.text:
                            if info_ad['funesbom'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, '#FUNESBOM', info_ad['funesbom'])

        for paragrafo in documento.paragraphs:
            texto = paragrafo.text
            if 'São Gonçalo' in texto:
                substituir_texto(paragrafo, 'São Gonçalo', dados_imovel['cidade'])

            if '#END_IMOVEL' in texto:
                substituir_texto(paragrafo, '#END_IMOVEL', dados_imovel['logradouro'] + ', ' + dados_imovel['numero'] + ', ' + dados_imovel['bairro'] + ', ' + dados_imovel['cidade'] + ' - ' + dados_imovel['estado'])
            
            if '#CEP' in texto:
                substituir_texto(paragrafo, '#CEP', dados_imovel['cep'])

            if porcentagem < 15:
                if 'fazer acordos, bem como receber ' in texto:
                    p_element = paragrafo._element
                    p_element.getparent().remove(p_element)

            if '#PERCENTUAL' in texto:
                substituir_texto(paragrafo, '#PERCENTUAL', str(porcentagem))

            if 'É #SUBROGA (facultada ou obrigatório)' in texto:
                if porcentagem == 12 or porcentagem == 15:
                    substituir_texto(paragrafo, '(facultada ou obrigatório)', 'facultada')

                if porcentagem == 20:
                    substituir_texto(paragrafo, '(facultada ou obrigatório)', 'obrigatório')
                    if 'Esta autorização é plenamente condedida' in texto:
                        remover_trecho(paragrafo, 'Esta autorização é plenamente concedida neste instrumento pela PARTE CONTRATANTE à PARTE CONTRATADA, autorizando que esta realize o pagamento pontual em qualquer tempo e frequência durante a vigência do contrato de locação.')

            if 'e material, de R$ 100,00 (R$50,00 se for no plano de 20%)' in texto:
                if porcentagem == 20:
                    substituir_texto(paragrafo, 'de R$ 100,00 (R$50,00 se for no plano de 20%)', 'R$ 50,00')
                else:
                    substituir_texto(paragrafo, 'de R$ 100,00 (R$50,00 se for no plano de 20%)', 'R$ 100,00')
        download.emit(documento)
        
    except Exception as e:
        error.emit('Erro ao gerar o contrato de Administração de Locação: ' + str(e))
