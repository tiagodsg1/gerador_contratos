import datetime

from docx import Document
from back.docx.src.inserir_tabelas import inserir_tabelas
from back.docx.src.retirar import delete_paragraph
from back.docx.src.retirar import retirar
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import remover_trecho
from back.docx.src.retirar import substituir_trecho_tabela

from back.bd.update.logs.log_corretor import LogCorretor

def locacao(dados_corretor, dados_imovel, caminho_documento, info_ad, sucesso, error, download):

    try:

        
    
        documento = Document(caminho_documento)

        inserir_tabelas(documento, documento.tables[2], info_ad['cliente1'])
        for table_index, table in enumerate(documento.tables):
            for row in table.rows:
                for cell in row.cells:
                    # Parte Imovel

                    if '#END_IMOVEL' in cell.text:
                        substituir_trecho_tabela(cell, '#END_IMOVEL', f"{dados_imovel['logradouro']}, {dados_imovel['numero']}, {dados_imovel['complemento']}, {dados_imovel['bairro']}, {dados_imovel['cidade']}, Rio de Janeiro")

                    if '#CEP' in cell.text:
                        substituir_trecho_tabela(cell, '#CEP', dados_imovel['cep'])

                    if '#MATRICULA' in cell.text:
                        if info_ad['matricula'] == '':
                            if dados_imovel['matricula'] == None:
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(cell, '#MATRICULA', dados_imovel['matricula'])
                        else:
                            substituir_trecho_tabela(cell, '#MATRICULA', info_ad['matricula'])

                    if '#CARTORIO' in cell.text:
                        if info_ad['cartorio'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#CARTORIO', info_ad['cartorio'])
                    
                    if '#INSCRICAO_IPTU' in cell.text:
                        if info_ad['n_iptu'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#INSCRICAO_IPTU', info_ad['n_iptu'])

                    if '#CONCESSIONARIA_LUZ' in cell.text:
                        if info_ad['luz'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#CONCESSIONARIA_LUZ', info_ad['luz'])

                    if '#RELOGIO' in cell.text:
                        if info_ad['relogio'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#RELOGIO', info_ad['relogio'])

                    if '#MONOBITRIFASICO' in cell.text:
                        if info_ad['monobitrifasico'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#MONOBITRIFASICO', info_ad['monobitrifasico'])

                    if '#CONCESSIONARIA_AGUA' in cell.text:
                        if info_ad['agua'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#CONCESSIONARIA_AGUA', info_ad['agua'])

                    if '#CONCESSIONARIA_GAS' in cell.text:
                        if info_ad['gas'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#CONCESSIONARIA_GAS', info_ad['gas'])

                    if '#FUNESBOM' in cell.text:
                        if info_ad['funesbom'] == '':
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(cell, '#FUNESBOM', info_ad['funesbom'])  
                    index = 2
                    for i in range(index):

                        if f'#{i}PARTE_CLIENTE' in cell.text:
                            substituir_trecho_tabela(cell, f'#{i}PARTE_CLIENTE', info_ad[f'cliente{i}']['nome'])
                        
                        if f'#{i}NACIONALIDADE' in cell.text:
                            substituir_trecho_tabela(cell, f'#{i}NACIONALIDADE', 'Brasileiro(a)')

                        if f'#{i}ESTADO CIVIL' in cell.text:
                            if info_ad[f'cliente{i}']['estado_civil'] == None:
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(cell, f'#{i}ESTADO CIVIL', info_ad[f'cliente{i}']['estado_civil'])
                        
                        if f'#{i}CPF' in cell.text:
                            if info_ad[f'cliente{i}']['cpf_cnpj'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(cell, f'#{i}CPF', info_ad[f'cliente{i}']['cpf_cnpj'])

                        if f'#{i}E_MAIL' in cell.text:
                            if info_ad[f'cliente{i}']['email'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(cell, f'#{i}E_MAIL', info_ad[f'cliente{i}']['email'])

                        if f'#{i}TELEFONE_LOCATARIA' in cell.text:
                            if info_ad[f'cliente{i}']['telefone'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(cell, f'#{i}TELEFONE_LOCATARIA', info_ad[f'cliente{i}']['telefone'])

                        if f'#{i}ENDEREÇO' in cell.text:
                            if info_ad[f'cliente{i}']['logradouro'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(cell, f'#{i}ENDEREÇO', f"{info_ad[f'cliente{i}']['logradouro']}, {info_ad[f'cliente{i}']['numero']}, {info_ad[f'cliente{i}']['bairro']}, {info_ad[f'cliente{i}']['cidade']}, Rio de Janeiro")
                        
                        if f'#{i}CEP' in cell.text:
                            if info_ad[f'cliente{i}']['cep'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(cell, f'#{i}CEP', info_ad[f'cliente{i}']['cep'])
                
                    #Locação
                    if '#PRAZOCONTRATO_EMMESES meses' in cell.text:
                        if int(info_ad['praz_contr']) == 1:
                            substituir_trecho_tabela(cell, '#PRAZOCONTRATO_EMMESES meses', f"{info_ad['praz_contr']} mês")
                        else:
                            substituir_trecho_tabela(cell, '#PRAZOCONTRATO_EMMESES meses', f"{info_ad['praz_contr']} meses")
                    
                    if '#INICIO_CONTRATO' in cell.text:
                        substituir_trecho_tabela(cell, '#INICIO_CONTRATO', info_ad['inicio_contr'])

                    if '#FINAL_CONTRATO' in cell.text:
                        substituir_trecho_tabela(cell, '#FINAL_CONTRATO', info_ad['fim_contr'])

                    if 'R$ #VALOR_ALUGUEL' in cell.text:
                        if info_ad['aluguel'] == None:
                            substituir_trecho_tabela(cell, 'R$ #VALOR_ALUGUEL', dados_imovel['valor'])
                        else:
                            substituir_trecho_tabela(cell, 'R$ #VALOR_ALUGUEL', info_ad['aluguel'])

                    if '#IPTU_MENSAL' in cell.text:
                        if info_ad['iptu'] == None:
                            if dados_imovel['valor_iptu'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(cell, '#IPTU_MENSAL', dados_imovel['valor_iptu'])
                        else:
                            substituir_trecho_tabela(cell, '#IPTU_MENSAL', info_ad['iptu'])

                    if '#CONDOMINIO_MENSAL' in cell.text:
                        if info_ad['cond'] == None:
                            if dados_imovel['valor_condominio'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(cell, '#CONDOMINIO_MENSAL', dados_imovel['valor_condominio'])
                        else:
                            substituir_trecho_tabela(cell, '#CONDOMINIO_MENSAL', info_ad['cond'])

                    if '#SEGURO_MENSAL' in cell.text:
                        substituir_trecho_tabela(cell, '#SEGURO_MENSAL', info_ad['seguro'])

                    if '#DIA_VENCIMENTO' in cell.text:
                        substituir_trecho_tabela(cell, '#DIA_VENCIMENTO', info_ad['data_venc'])

        #Texto do documento
        for paragraph in documento.paragraphs:
            retirar(paragraph)
            text = paragraph.text
            
            if "#CODIGO_CONTRATO" in text:
                substituir_texto(paragraph, '#CODIGO_CONTRATO', dados_imovel['referencia'])
            
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
                valor = '1 Pessoa(as)' if info_ad['max_moradores'] is None else info_ad['max_moradores']
                substituir_texto(paragraph, '#MAXIMO_MORADORES', valor)
            
            if 'Cabe à PARTE LOCATÁRIA cumprir diligentemente ' in text:
                if info_ad['cond'] == None: #Rever
                    delete_paragraph(paragraph)
            
            if 'Não é permitida a criação, manutenção, guarda' in text:
                
                if info_ad['act_anm'] == True:
                    delete_paragraph(paragraph)

            if 'O Relatório de Vistoria será elaborado ' in text:
                
                if info_ad['vist_agr'] == True:
                    remover_trecho(paragraph, 'O Relatório de Vistoria será elaborado antes da entrega das chaves, sendo enviado à PARTE LOCATÁRIA para ciência, e passará a ser parte integrante deste contrato /')
                else:
                    remover_trecho(paragraph, '/ O Relatório de Vistoria segue anexo ao presente contrato, sendo parte integrante deste')

            if 'Caso o relatório de vistoria não seja assinado por todos da PARTE LOCATÁRIA' in text:
                
                if info_ad['vist_agr'] == True:
                    delete_paragraph(paragraph)

            if '#FORO' in text:
                substituir_texto(paragraph, '#FORO', dados_imovel['cidade'])

        list_envio = [
            dados_corretor['nome'],
            dados_corretor['id'],
            dados_corretor['creci'],
            'INSERT',
            'Locação Residencial',
            datetime.datetime.now().strftime("%d/%m/%Y"),
            dados_imovel['referencia'],
            dados_imovel['bairro'],
            dados_imovel['cidade'],
            dados_imovel['id'],
            info_ad['cliente0']['nome'],
            info_ad['cliente0']['bairro'],
            info_ad['cliente0']['cidade'],
            info_ad['cliente0']['id'] ]
        
        log_corretor = LogCorretor()
        log_corretor.insert_logs(list_envio)

        download.emit(documento)
    except Exception as e:
        error.emit(str(e))