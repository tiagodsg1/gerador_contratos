from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt

from back.docx.src.retirar import delete_paragraph
from back.docx.src.retirar import retirar

def locacao(dados_cliente, dados_corretor, dados_imovel, dados_cliente2, caminho_documento, info_ad, sucesso, error, download):

    try:
    
        documento = Document(caminho_documento)
        for table_index, table in enumerate(documento.tables):
            for row in table.rows:
                for cell in row.cells:
                    # Parte Imovel
                    if '#END_IMOVEL' in cell.text:
                        cell.text = cell.text.replace('#END_IMOVEL', f'{dados_imovel['logradouro']}, {dados_imovel['numero']}, {dados_imovel['complemento']}, {dados_imovel['bairro']}, {dados_imovel['cidade']}, Rio de Janeiro')
                    if '#CEP' in cell.text:
                        cell.text = cell.text.replace('#CEP', dados_imovel['cep'])

                    if '#MATRICULA' in cell.text:
                        if info_ad['matricula'] == '':
                            if dados_imovel['matricula'] == None:
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                cell.text = cell.text.replace('#MATRICULA', dados_imovel['matricula'])
                        else:
                            cell.text = cell.text.replace('#MATRICULA', info_ad['matricula'])

                    if '#CARTORIO' in cell.text:
                        if info_ad['cartorio'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#CARTORIO', info_ad['cartorio'])
                    
                    if '#INSCRICAO_IPTU' in cell.text:
                        if info_ad['n_iptu'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#INSCRICAO_IPTU', info_ad['n_iptu'])

                    if '#CONCESSIONARIA_LUZ' in cell.text:
                        if info_ad['luz'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#CONCESSIONARIA_LUZ', info_ad['luz'])

                    if '#RELOGIO' in cell.text:
                        if info_ad['relogio'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#RELOGIO', info_ad['relogio'])

                    if '#MONOBITRIFASICO' in cell.text:
                        if info_ad['monobitrifasico'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#MONOBITRIFASICO', info_ad['monobitrifasico'])

                    if '#AGUA' in cell.text:
                        if info_ad['agua'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#AGUA', info_ad['agua'])

                    if '#CONCESSIONARIA_GAS' in cell.text:
                        if info_ad['gas'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#CONCESSIONARIA_GAS', info_ad['gas'])

                    if '#2FUNESBOM_MENSAL' in cell.text:
                        if info_ad['funesbom'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#2FUNESBOM_MENSAL', info_ad['funesbom'])          
                    # Parte Locadora

                    if '#PARTE_LOCADORA' in cell.text:
                        cell.text = cell.text.replace('#PARTE_LOCADORA', dados_cliente['nome'])
                    
                    if '#NACIONALIDADE' in cell.text:
                        cell.text = cell.text.replace('#NACIONALIDADE', 'Brasileiro(a)')
                    
                    if '#ESTADO CIVIL' in cell.text:
                        if dados_cliente['estado_civil'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#ESTADO CIVIL', dados_cliente['estado_civil'])
                    
                    if '#CPF' in cell.text:
                        if dados_cliente['cpf_cnpj'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#CPF', dados_cliente['cpf_cnpj'])
                    
                    #Parte Locataria

                    if '#PARTE_LOCATARIA' in cell.text:
                        cell.text = cell.text.replace('#PARTE_LOCATARIA', dados_cliente['nome'])
                    
                    if '#2NACIONALIDADE' in cell.text:
                        cell.text = cell.text.replace('#2NACIONALIDADE', 'Brasileiro(a)')

                    if '#2ESTADO CIVIL' in cell.text:
                        if dados_cliente['estado_civil'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#2ESTADO CIVIL', dados_cliente['estado_civil'])
                    
                    if '#2CPF' in cell.text:
                        if dados_cliente['cpf_cnpj'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#2CPF', dados_cliente['cpf_cnpj'])

                    if '#2E_MAIL' in cell.text:
                        if dados_cliente['email'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#2E_MAIL', dados_cliente['email'])

                    if '#TELEFONE_LOCATARIA' in cell.text:
                        if dados_cliente['telefone'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#TELEFONE_LOCATARIA', dados_cliente['telefone'])

                    if '#2ENDEREÇO' in cell.text:
                        if dados_cliente['logradouro'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#2ENDEREÇO', f'{dados_cliente['logradouro']}, {dados_cliente['numero']}, {dados_cliente['bairro']}, {dados_cliente['cidade']}, Rio de Janeiro')
                    
                    if '#2CEP' in cell.text:
                        if dados_cliente['cep'] == 'None':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            cell.text = cell.text.replace('#2CEP', dados_cliente['cep'])

                    if '#1PARTE_LOCATARIA' in cell.text:
                        cell.text = cell.text.replace('#1PARTE_LOCATARIA', dados_cliente['nome'])
                        for paragrafo in cell.paragraphs:
                            if cell.text in paragrafo.text:
                                paragrafo.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                
                    #Locação

                    if '#PRAZOCONTRATO_EMMESES meses' in cell.text:
                        if int(info_ad['praz_contr']) == 1:
                            cell.text = cell.text.replace('#PRAZOCONTRATO_EMMESES meses', f'{info_ad['praz_contr']} mês')
                        else:
                            cell.text = cell.text.replace('#PRAZOCONTRATO_EMMESES meses', f'{info_ad['praz_contr']} meses')
                    
                    if '#INICIO_CONTRATO' in cell.text:
                        cell.text = cell.text.replace('#INICIO_CONTRATO', info_ad['inicio_contr'])

                    if '#FINAL_CONTRATO' in cell.text:
                        cell.text = cell.text.replace('#FINAL_CONTRATO', info_ad['fim_contr'])

                    if '#VALOR_ALUGUEL' in cell.text:
                        if info_ad['aluguel'] == None:
                            cell.text = cell.text.replace('#VALOR_ALUGUEL R$', dados_imovel['valor'])
                        else:
                            cell.text = cell.text.replace('#VALOR_ALUGUEL', info_ad['aluguel'])

                    if '#IPTU_MENSAL' in cell.text:
                        if info_ad['iptu'] == None:
                            if dados_imovel['valor_iptu'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                cell.text = cell.text.replace('#IPTU_MENSAL', dados_imovel['valor_iptu'])
                        else:
                            cell.text = cell.text.replace('#IPTU_MENSAL', info_ad['iptu'])

                    if '#CONDOMINIO_MENSAL' in cell.text:
                        if info_ad['cond'] == None:
                            if dados_imovel['valor_condominio'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                cell.text = cell.text.replace('#CONDOMINIO_MENSAL', dados_imovel['valor_condominio'])
                        else:
                            cell.text = cell.text.replace('#CONDOMINIO_MENSAL', info_ad['cond'])

                    if '#SEGURO_MENSAL' in cell.text:
                        cell.text = cell.text.replace('#SEGURO_MENSAL', info_ad['seguro'])

        #Texto do documento
        for paragraph in documento.paragraphs:
            retirar(paragraph)
            text = paragraph.text
            if 'Entretanto, como a data de assinatura é diferente da data da entrega das chaves, o período de ' in text:
                if info_ad['chav_agr'] == True :
                    delete_paragraph(paragraph)

            if 'A PARTE LOCATÁRIA tem direito a uso de uma vaga de garagem.' in text:
                if info_ad['garagem'] == False:
                    delete_paragraph(paragraph)

            if 'A PARTE LOCATÁRIA tem ciência de que o imóvel está gravado com alienação fiduciária' in text:
                if info_ad['alienado'] == False:
                    delete_paragraph(paragraph)
                    
            if 'Juntamente com o aluguel serão pagos pela PARTE LOCATÁRIA todos os impostos,' in text:
                if info_ad['enc_loc'] == False:
                    delete_paragraph(paragraph)

            if 'Se a PARTE LOCATÁRIA quiser' in text:
                if info_ad['enc_loc'] == False:
                    delete_paragraph(paragraph)

            if 'Havendo cobrança adicional na cota condominial' in text:
                if info_ad['fic_cond'] == False:
                    delete_paragraph(paragraph) 

            if 'Os locatários são integralmente solidários ' in text:
                if info_ad['max_moradores'] == None:
                    delete_paragraph(paragraph)
            
            if '#MAXIMO_MORADORES' in text:
                if info_ad['max_moradores'] == None:
                    text.replace('#MAXIMO_MORADORES pessoas', '1 pessoa(s)')   
                else:
                    paragraph.text = paragraph.text.replace('#MAXIMO_MORADORES', info_ad['max_moradores'])
            
            if 'Cabe à PARTE LOCATÁRIA cumprir diligentemente ' in text:
                if info_ad['cond'] == None: #Rever
                    delete_paragraph(paragraph)
            
            if 'Não é permitida a criação, manutenção, guarda' in text:
                if info_ad['act_anm'] == True:
                    delete_paragraph(paragraph)

            if 'O Relatório de Vistoria será elaborado ' in text:
                if info_ad['vist_agr'] == True:
                    text.replace('O Relatório de Vistoria será elaborado antes da entrega das chaves, sendo enviado à PARTE LOCATÁRIA para ciência, e passará a ser parte integrante deste contrato', '')
                else:
                    text.replace('O Relatório de Vistoria segue anexo ao presente contrato, sendo parte integrante deste', '')

            if 'Caso o relatório de vistoria não seja assinado por todos da PARTE LOCATÁRIA' in text:
                if info_ad['vist_agr'] == True:
                    delete_paragraph(paragraph)

        download.emit(documento)
    except Exception as e:
        error.emit(str(e))