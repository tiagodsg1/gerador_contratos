from docx import Document

from back.docx.src.inserir_tabelas import inserir_tabelas
from back.docx.src.retirar import retirar
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import remover_trecho
from back.docx.src.retirar import substituir_trecho_tabela
    
def administracao_locacao( dados_corretor, dados_imovel, info_ad, caminho_documento, sucesso, error, download):

    try:

        documento = Document(caminho_documento)
        porcentagem = int(info_ad['porcentagem'])

        inserir_tabelas(documento, documento.tables[1], info_ad['cliente1'])

        index = 1
        if info_ad['cliente1'] != None:
            index = 2
            
        for tabela_index, tabela in enumerate(documento.tables):
            for linha in tabela.rows:
                for celula in linha.cells:
                    for i in range(index):
                        if f'#{i}PARTE_LOCADORA' == celula.text:
                            substituir_trecho_tabela(celula, f'#{i}PARTE_LOCADORA', info_ad[f'cliente{i}']['nome'])

                        if f'#{i}PARTE_LOCADORA_ASSINATURA' in celula.text:
                            substituir_trecho_tabela(celula, f'#{i}PARTE_LOCADORA_ASSINATURA', info_ad[f'cliente{i}']['nome'])

                        if f'#{i}NACIONALIDADE' == celula.text:
                            substituir_trecho_tabela(celula, f'#{i}NACIONALIDADE', 'Brasileiro')

                        if f'#{i}ESTADO CIVIL' == celula.text:
                            if info_ad[f'cliente{i}']['estado_civil'] == None:
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)

                            else:
                                substituir_trecho_tabela(celula, f'#{i}ESTADO CIVIL', info_ad[f'cliente{i}']['estado_civil'])

                        if f'#{i}CPF' == celula.text:
                            if info_ad[f'cliente{i}']['cpf_cnpj'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, f'#{i}CPF', info_ad[f'cliente{i}']['cpf_cnpj'])

                        if f'#{i}E_MAIL' == celula.text:
                            if info_ad[f'cliente{i}']['email'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, f'#{i}E_MAIL', info_ad[f'cliente{i}']['email'])

                        if f'#{i}ENDERECO' == celula.text:
                            if info_ad[f'cliente{i}']['logradouro'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, f'#{i}ENDERECO', info_ad[f'cliente{i}']['logradouro'])

                        if f'#{i}CEP' == celula.text:
                            if info_ad[f'cliente{i}']['cep'] == 'None':
                                tabela_para_remover = documento.tables[tabela_index]
                                remover_linha = tabela_para_remover.rows[linha._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, f'#{i}CEP', info_ad[f'cliente{i}']['cep'])

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
            retirar(paragrafo)
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
