from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import os

from back.docx.src.inserir_tabelas import inserir_tabelas
    
def administracao_locacao(dados_cliente, dados_imovel, dados_cliente2, dados_cliente3, info_ad, caminho_documento, sucesso, error, percentual, download):

    try:

        documento = Document(caminho_documento)
        print('Caminho do documento:', caminho_documento)
        porcentagem = int(percentual)

        inserir_tabelas(documento, documento.tables[0], dados_cliente2, dados_cliente3)
            
        for tabela_index, tabela in enumerate(documento.tables):
            for linha in tabela.rows:
                for celula in linha.cells:
                    if dados_cliente:
                        #Parte do Cliente
                        if '#1PARTE_LOCADORA' == celula.text:
                            celula.text = celula.text.replace('#1PARTE_LOCADORA', dados_cliente['nome'])

                        if '#PARTE_LOCADORA_ASSINATURA' in celula.text:
                            celula.text = celula.text.replace('#PARTE_LOCADORA_ASSINATURA', dados_cliente['nome'])
                            for paragrafo in celula.paragraphs:
                                if celula.text in paragrafo.text:
                                    paragrafo.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

                        if '#NACIONALIDADE' == celula.text:
                            celula.text = celula.text.replace('#NACIONALIDADE', 'Brasileiro')

                        if '#ESTADO CIVIL' == celula.text:
                            if dados_cliente['estado_civil'] == None:
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)

                            else:
                                celula.text = celula.text.replace('#ESTADO CIVIL', dados_cliente['estado_civil'])

                        if '#CPF' == celula.text:
                            if dados_cliente['cpf_cnpj'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#CPF', dados_cliente['cpf_cnpj'])

                        if '#E_MAIL' == celula.text:
                            if dados_cliente['email'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#E_MAIL', dados_cliente['email'])

                        if '#ENDERECO' == celula.text:
                            if dados_cliente['logradouro'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#ENDERECO', dados_cliente['logradouro'])

                        if '#1CEP' == celula.text:
                            if dados_cliente['cep'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#1CEP', dados_cliente['cep'])
                    
                    if dados_cliente2:
                        if '#2PARTE_CLIENTE' == celula.text:
                            celula.text = celula.text.replace('#2PARTE_CLIENTE', dados_cliente2['nome'])

                        if '#2PARTE_CLIENTE_ASSINATURA' in celula.text:
                            celula.text = celula.text.replace('#2PARTE_CLIENTE_ASSINATURA', dados_cliente2['nome'])
                            for paragrafo in celula.paragraphs:
                                if celula.text in paragrafo.text:
                                    paragrafo.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                        
                        if '#2NACIONALIDADE' == celula.text:
                            celula.text = celula.text.replace('#2NACIONALIDADE', 'Brasileiro')

                        if '#2ESTADO CIVIL' == celula.text:
                            if dados_cliente2['estado_civil'] == None:
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#2ESTADO CIVIL', dados_cliente2['estado_civil'])

                        if '#2CPF' == celula.text:
                            if dados_cliente2['cpf_cnpj'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#2CPF', dados_cliente2['cpf_cnpj'])
                        
                        if '#2E_MAIL' == celula.text:
                            if dados_cliente2['email'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#2E_MAIL', dados_cliente2['email'])
                        
                        if '#2ENDERECO' == celula.text:
                            if dados_cliente2['logradouro'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#2ENDERECO', dados_cliente2['logradouro'])

                        if '#2CEP' == celula.text:
                            if dados_cliente2['cep'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#2CEP', dados_cliente2['cep'])
                        
                    if dados_cliente3:
                        if '#3PARTE_CLIENTE' == celula.text:
                            celula.text = celula.text.replace('#3PARTE_CLIENTE', dados_cliente3['nome'])

                        if '#3PARTE_CLIENTE_ASSININATURA' in celula.text:
                            celula.text = celula.text.replace('#3PARTE_CLIENTE_ASSININATURA', dados_cliente3['nome'])
                            for paragrafo in celula.paragraphs:
                                if celula.text in paragrafo.text:
                                    paragrafo.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                        
                        if '#3NACIONALIDADE' == celula.text:
                            celula.text = celula.text.replace('#3NACIONALIDADE', 'Brasileiro')

                        if '#3ESTADO CIVIL' == celula.text:
                            if dados_cliente3['estado_civil'] == None:
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#3ESTADO CIVIL', dados_cliente3['estado_civil'])

                        if '#3CPF' == celula.text:
                            if dados_cliente3['cpf_cnpj'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#3CPF', dados_cliente3['cpf_cnpj'])
                        
                        if '#3E_MAIL' == celula.text:
                            if dados_cliente3['email'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#3E_MAIL', dados_cliente3['email'])
                        
                        if '#3ENDERECO' == celula.text:
                            if dados_cliente3['logradouro'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#3ENDERECO', dados_cliente3['logradouro'])

                        if '#3CEP' == celula.text:
                            if dados_cliente3['cep'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#3CEP', dados_cliente3['cep'])

                    if dados_imovel:
                        #Parte do Imóvel
                        if '#CARTORIO' == celula.text:
                            if info_ad['cartorio'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#CARTORIO', info_ad['cartorio'])

                        if '#MATRICULA' in celula.text:
                            if info_ad['matricula'] == '':
                                if dados_imovel['matricula'] == None:
                                    tabela_remove = documento.tables[tabela_index]
                                    remover_linha = tabela_remove.rows[linha._index]._element
                                    remover_linha.getparent().remove(remover_linha)
                                else:
                                    celula.text = celula.text.replace('#MATRICULA', dados_imovel['matricula'])
                            else:
                                celula.text = celula.text.replace('#MATRICULA', info_ad['matricula'])

                        if '#INSCRICAO_IPTU' == celula.text:
                            if info_ad['n_iptu'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#INSCRICAO_IPTU', info_ad['n_iptu'])        

                        if '#CONCESSIONARIA_LUZ' == celula.text:
                            if info_ad['luz'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#CONCESSIONARIA_LUZ', info_ad['luz'])
            
                        if '#RELOGIO' == celula.text:
                            if info_ad['relogio'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#RELOGIO', info_ad['relogio'])

                        if '#MONOBITRIFASICO' == celula.text:
                            if info_ad['monobitrifasico'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#MONOBITRIFASICO', info_ad['monobitrifasico'])

                        if '#CONCESSIONARIA_GAS' == celula.text:
                            if info_ad['gas']== '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#CONCESSIONARIA_GAS', info_ad['gas'])

                        if '#FUNESBOM' == celula.text:
                            if info_ad['funesbom'] == '':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                celula.text = celula.text.replace('#FUNESBOM', info_ad['funesbom'])

        for paragrafo in documento.paragraphs:
            if 'São Gonçalo' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('São Gonçalo', dados_imovel['cidade'])

            if '#END_IMOVEL' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#END_IMOVEL', dados_imovel['logradouro'] + ', ' + dados_imovel['numero'] + ', ' + dados_imovel['bairro'] + ', ' + dados_imovel['cidade'] + ' - ' + dados_imovel['estado'])
            
            if '#CEP' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#CEP', dados_imovel['cep'])

            if porcentagem < 15:
                if 'fazer acordos, bem como receber ' in paragrafo.text:
                    p_element = paragrafo._element
                    p_element.getparent().remove(p_element)

            if '#PERCENTUAL' in paragrafo.text:
                paragrafo.text = paragrafo.text.replace('#PERCENTUAL', str(porcentagem))

            if 'É #SUBROGA (facultada ou obrigatório)' in paragrafo.text:
                if porcentagem == 12 or porcentagem == 15:
                    paragrafo.text = paragrafo.text.replace('(facultada ou obrigatório)', 'facultada')

                if porcentagem == 20:
                    paragrafo.text = paragrafo.text.replace('(facultada ou obrigatório)', 'obrigatório')
                    if 'Esta autorização é plenamente condedida' in paragrafo.text:
                        paragrafo.text = paragrafo.text.replace('Esta autorização é plenamente concedida neste instrumento pela PARTE CONTRATANTE à PARTE CONTRATADA, autorizando que esta realize o pagamento pontual em qualquer tempo e frequência durante a vigência do contrato de locação.', " ")

            if 'e material, de R$ 100,00 (R$50,00 se for no plano de 20%)' in paragrafo.text:
                if porcentagem == 20:
                    paragrafo.text = paragrafo.text.replace('de R$ 100,00 (R$50,00 se for no plano de 20%)', 'R$ 50,00')
                else:
                    paragrafo.text = paragrafo.text.replace('de R$ 100,00 (R$50,00 se for no plano de 20%)', 'R$ 100,00')
        download.emit(documento)
        
    except Exception as e:
        print(e)
