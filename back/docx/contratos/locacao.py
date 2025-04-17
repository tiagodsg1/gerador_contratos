import datetime
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from docx import Document
from back.docx.src.retirar import delete_paragraph
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import remover_trecho
from back.docx.src.retirar import substituir_trecho_tabela

from back.bd.update.logs.log_corretor import LogCorretor

def locacao(dados_corretor, dados_imovel, caminho_documento, info_ad, sucesso, error, download):
    try:
        documento = Document(caminho_documento)
    
        inserir_tabelas(documento, documento.tables, info_ad['cliente2'], info_ad['cliente3'])
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
                    if info_ad['cliente2'] != None or info_ad['cliente3'] != None:
                        index = 3
                    if info_ad['cliente3'] != None and info_ad['cliente2'] != None:
                        index = 4
                    # Parte Locatária
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

                    if 'R$ #2FUNESBOM_MENSAL' in cell.text:
                        substituir_trecho_tabela(cell, 'R$ #2FUNESBOM_MENSAL', info_ad['n_funesbom'])

        #Texto do documento
        for paragraph in documento.paragraphs:
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
        error.emit(f"Erro ao gerar o contrato de locação: {e}")


def inserir_tabelas(documento, tabela, dados_cliente2, dados_cliente3):

    if dados_cliente2:
        tabela_existente = tabela[2]
        elemento_tabela = tabela_existente._element

        tabela_vazia = documento.add_table(rows=1, cols=1)
        elemento_tabela_vazia = tabela_vazia._element
        elemento_tabela.addnext(elemento_tabela_vazia)

        tabela_cliente2 = documento.add_table(rows=7, cols=2)

        column_widths = [Cm(9.25), Cm(20)]  # Defina a largura de cada coluna

        for col_index, width in enumerate(column_widths):
            for cell in tabela_cliente2.columns[col_index].cells:
                cell.width = width

        tabela_cliente2.rows[0].cells[0].text = 'Nome'
        tabela_cliente2.rows[1].cells[0].text = 'Nacionalidade'
        tabela_cliente2.rows[2].cells[0].text = 'Estado Civil'
        tabela_cliente2.rows[3].cells[0].text = 'CPF'
        tabela_cliente2.rows[4].cells[0].text = 'E-mail'
        tabela_cliente2.rows[5].cells[0].text = 'Endereço'
        tabela_cliente2.rows[6].cells[0].text = 'CEP'

        tabela_cliente2.rows[0].cells[1].text = '#2PARTE_CLIENTE'
        tabela_cliente2.rows[1].cells[1].text = '#2NACIONALIDADE'
        tabela_cliente2.rows[2].cells[1].text = '#2ESTADO CIVIL'
        tabela_cliente2.rows[3].cells[1].text = '#2CPF'
        tabela_cliente2.rows[4].cells[1].text = '#2E_MAIL'
        tabela_cliente2.rows[5].cells[1].text = '#2ENDEREÇO'
        tabela_cliente2.rows[6].cells[1].text = '#2CEP'

        elemento_tabela_vazia.addnext(tabela_cliente2._element)
        tabela_cliente2.style = tabela_existente.style

        total_tabelas = len(documento.tables)
        tabela_assinatura = documento.tables[total_tabelas - 1]
        elemento_tabela_assinatura = tabela_assinatura._element

        tabela_assinatura_new_cliente = documento.add_table(rows=1, cols=2)

        elemento_tabela_assinatura_new_cliente = tabela_assinatura_new_cliente._element
        tabela_assinatura_new_cliente.rows[0].cells[0].text = '\n_____________________________________________________\n#2PARTE_CLIENTE\nPARTE CONTRATANTE'
        for i in range(2):
            for paragraph in tabela_assinatura_new_cliente.rows[0].cells[i].paragraphs:
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                for run in paragraph.runs:
                    run.font.size = Pt(12)
                    run.bold = True

        for row in tabela_cliente2.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.size = Pt(12)
                        run.bold = True

        elemento_tabela_assinatura.addnext(elemento_tabela_assinatura_new_cliente)
        add_table_borders(tabela_cliente2)

    if dados_cliente3:
        tabela_existente = tabela[1]
        elemento_tabela = tabela_existente._element

        tabela_vazia = documento.add_table(rows=1, cols=1)
        elemento_tabela_vazia = tabela_vazia._element
        elemento_tabela.addnext(elemento_tabela_vazia)

        tabela_cliente3 = documento.add_table(rows=7, cols=2)

        column_widths = [Cm(9.25), Cm(20)]  # Defina a largura de cada coluna

        for col_index, width in enumerate(column_widths):
            for cell in tabela_cliente3.columns[col_index].cells:
                cell.width = width

        tabela_cliente3.rows[0].cells[0].text = 'Nome'
        tabela_cliente3.rows[1].cells[0].text = 'Nacionalidade'
        tabela_cliente3.rows[2].cells[0].text = 'Estado Civil'
        tabela_cliente3.rows[3].cells[0].text = 'CPF'
        tabela_cliente3.rows[4].cells[0].text = 'E-mail'
        tabela_cliente3.rows[5].cells[0].text = 'Endereço'
        tabela_cliente3.rows[6].cells[0].text = 'CEP'

        tabela_cliente3.rows[0].cells[1].text = '#3PARTE_CLIENTE'
        tabela_cliente3.rows[1].cells[1].text = '#3NACIONALIDADE'
        tabela_cliente3.rows[2].cells[1].text = '#3ESTADO CIVIL'
        tabela_cliente3.rows[3].cells[1].text = '#3CPF'
        tabela_cliente3.rows[4].cells[1].text = '#3E_MAIL'
        tabela_cliente3.rows[5].cells[1].text = '#3ENDEREÇO'
        tabela_cliente3.rows[6].cells[1].text = '#3CEP'

        elemento_tabela_vazia.addnext(tabela_cliente3._element)
        tabela_cliente3.style = tabela_existente.style
        for row in tabela_cliente3.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.size = Pt(12)
                        run.bold = True
        
        add_table_borders(tabela_cliente3)

def add_table_borders(table):
    """
    Adiciona bordas à tabela.
    """
    tbl = table._element  # Obtenha o elemento XML subjacente da tabela
    tbl_pr = tbl.tblPr  # Acesse as propriedades da tabela
    tbl_borders = OxmlElement('w:tblBorders')

    for border in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border_el = OxmlElement(f'w:{border}')
        border_el.set(qn('w:val'), 'single')  # Tipo de borda
        border_el.set(qn('w:sz'), '4')  # Espessura (em oitavos de ponto)
        border_el.set(qn('w:space'), '0')  # Espaçamento
        border_el.set(qn('w:color'), '000000')  # Cor (hexadecimal)
        tbl_borders.append(border_el)

    tbl_pr.append(tbl_borders)