from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

from back.docx.src.inserir_tabelas import inserir_tabelas
from back.docx.src.retirar import retirar
from back.docx.src.retirar import delete_paragraph
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import substituir_trecho_tabela

def compra_venda(caminho_documento, dados_imovel, dados_corretor, info_ad, sucesso, error, download):
    try:
        documento = Document(caminho_documento)
        inserir_tabelas(documento, documento.tables, info_ad['cliente2'], info_ad['cliente3'])
        index = 2
        if info_ad['cliente2'] != None or info_ad['cliente3'] != None:
            index = 3
        if info_ad['cliente2'] != None and info_ad['cliente3'] != None:
            index = 4

        for table_index, tabela in enumerate(documento.tables):
            for row in tabela.rows:
                for celula in row.cells:
                    for i in range(index):
                        if f"#{i}PARTE_CLIENTE" in celula.text:
                            substituir_trecho_tabela(celula, f"#{i}PARTE_CLIENTE", info_ad[f'cliente{i}']['nome'])

                        if f'#{i}NACIONALIDADE' in celula.text:
                                substituir_trecho_tabela(celula, f'#{i}NACIONALIDADE', 'Brasileiro(a)')
                        
                        if f'#{i}ESTADO CIVIL' in celula.text:
                            if info_ad[f'cliente{i}']['estado_civil'] == None:
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, 'ESTADO CIVIL', info_ad[f'cliente{i}']['estado_civil'])
                        
                        if f'#{i}CPF' in celula.text:
                            if info_ad[f'cliente{i}']['cpf_cnpj'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, f'#{i}CPF', info_ad[f'cliente{i}']['cpf_cnpj'])

                        if f'#{i}E_MAIL' in celula.text:
                            if info_ad[f'cliente{i}']['email'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, f'#{i}E_MAIL', info_ad[f'cliente{i}']['email'])

                        if f'#{i}ENDEREÇO' in celula.text:
                            if info_ad[f'cliente{i}']['logradouro'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, f'#{i}ENDEREÇO', f"{info_ad[f'cliente{i}']['logradouro']}, {info_ad[f'cliente{i}']['numero']}, {info_ad[f'cliente{i}']['bairro']}")
                        
                        if f'#{i}CEP' in celula.text:
                            if info_ad[f'cliente{i}']['cep'] == 'None':
                                tabela_remove = documento.tables[table_index]
                                remover_linha = tabela_remove.rows[row._index]._element
                                remover_linha.getparent().remove(remover_linha)
                            else:
                                substituir_trecho_tabela(celula, f'#{i}CEP', info_ad[f'cliente{i}']['cep'])

                    #Dados do imóvel
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

                    if '#4CEP' in celula.text:
                        if dados_imovel['cep'] == None:
                            tabela_remove = documento.tables[table_index]
                            remover_linha = tabela_remove.rows[row._index]._element
                            remover_linha.getparent().remove(remover_linha)

                        else:
                            substituir_trecho_tabela(celula, '#4CEP', dados_imovel['cep'])

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
            texto = paragrafo.text
            '''if '#CODIGO_CONTRATO' in texto:
                substituir_texto(paragrafo, '#CODIGO_CONTRATO', dados_imovel['matricula'])'''

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

def inserir_tabelas(documento, tabela, dados_cliente2, dados_cliente3):

    if dados_cliente2:
        tabela_existente = tabela[0]
        elemento_tabela = tabela_existente._element

        tabela_vazia = documento.add_table(rows=1, cols=1)
        elemento_tabela_vazia = tabela_vazia._element
        elemento_tabela.addnext(elemento_tabela_vazia)

        tabela_cliente2 = documento.add_table(rows=7, cols=2)

        column_widths = [Cm(7.25), Cm(20)]  # Defina a largura de cada coluna

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
        tabela_assinatura_new_cliente.rows[0].cells[0].text = '\n_________________________________\n#2PARTE_CLIENTE\nPARTE CONTRATANTE'
        for i in range(2):
            for paragraph in tabela_assinatura_new_cliente.rows[0].cells[i].paragraphs:
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                for run in paragraph.runs:
                    run.font.size = Pt(12)

        for row in tabela_cliente2.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    for run in paragraph.runs:
                        run.font.size = Pt(12)

        if dados_cliente3:
            tabela_existente = tabela[1]
            elemento_tabela = tabela_existente._element

            tabela_vazia = documento.add_table(rows=1, cols=1)
            elemento_tabela_vazia = tabela_vazia._element
            elemento_tabela.addnext(elemento_tabela_vazia)

            tabela_cliente2 = documento.add_table(rows=7, cols=2)

            column_widths = [Cm(7.25), Cm(20)]  # Defina a largura de cada coluna

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

            tabela_cliente2.rows[0].cells[1].text = '#3PARTE_CLIENTE'
            tabela_cliente2.rows[1].cells[1].text = '#3NACIONALIDADE'
            tabela_cliente2.rows[2].cells[1].text = '#3ESTADO CIVIL'
            tabela_cliente2.rows[3].cells[1].text = '#3CPF'
            tabela_cliente2.rows[4].cells[1].text = '#3E_MAIL'
            tabela_cliente2.rows[5].cells[1].text = '#3ENDEREÇO'
            tabela_cliente2.rows[6].cells[1].text = '#3CEP'

            elemento_tabela_vazia.addnext(tabela_cliente2._element)
            tabela_cliente2.style = tabela_existente.style

            total_tabelas = len(documento.tables)
            tabela_assinatura = documento.tables[total_tabelas - 1]
            elemento_tabela_assinatura = tabela_assinatura._element

            tabela_assinatura_new_cliente = documento.add_table(rows=1, cols=2)

            elemento_tabela_assinatura_new_cliente = tabela_assinatura_new_cliente._element
            tabela_assinatura_new_cliente.rows[0].cells[0].text = '\n_________________________________\n#3PARTE_CLIENTE\nPARTE CONTRATANTE'
            for i in range(2):
                for paragraph in tabela_assinatura_new_cliente.rows[0].cells[i].paragraphs:
                    paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
                    for run in paragraph.runs:
                        run.font.size = Pt(12)

            for row in tabela_cliente2.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        for run in paragraph.runs:
                            run.font.size = Pt(12)


            elemento_tabela_assinatura.addnext(elemento_tabela_assinatura_new_cliente)
            add_table_borders(tabela_cliente2)
                    

