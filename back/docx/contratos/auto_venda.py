from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx import Document

from back.docx.src.retirar import retirar
from back.docx.src.retirar import substituir_texto
from back.docx.src.retirar import remover_trecho
from back.docx.src.retirar import substituir_trecho_tabela


def auto_venda(caminho_documento, dados_corretor, dados_imovel, info_ad, sucesso, error, download):
    '''try:'''
    documento = Document(caminho_documento)

    inserir_tabelas(documento, documento.tables[0], info_ad['cliente1'])
    index = 1
    if info_ad['cliente1'] != None:
        index = 2
    
    for tabela_index, tabela in enumerate(documento.tables):
        for linha in tabela.rows:
            for celula in linha.cells:
                for i in range(index):
                    #Dados do cliente
                    if f'#{i}PARTE_CLIENTE' in celula.text:
                        substituir_trecho_tabela(celula, f'#{i}PARTE_CLIENTE', info_ad[f'cliente{i}']['nome'])
                    
                    if f'#{i}NACIONALIDADE' in celula.text:
                        substituir_trecho_tabela(celula, f'#{i}NACIONALIDADE', 'Brasileiro(a)')

                    if f'#{i}ESTADO CIVIL' in celula.text:
                        if info_ad[f'cliente{i}']['estado_civil'] == None:
                            tabela_remove = documento.tables[tabela_index]
                            remover_linha = tabela_remove.rows[linha._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, f'#{i}ESTADO CIVIL', info_ad[f'cliente{i}']['estado_civil'])
                    
                    if f'#{i}CPF' in celula.text:
                        if info_ad[f'cliente{i}']['cpf_cnpj'] == 'None':
                            tabela_remove = documento.tables[tabela_index]
                            remover_linha = tabela_remove.rows[linha._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, f'#{i}CPF', info_ad[f'cliente{i}']['cpf_cnpj'])
                    
                    if f'#{i}E_MAIL' in celula.text:
                        if info_ad[f'cliente{i}']['email'] == 'None':
                            tabela_remove = documento.tables[tabela_index]
                            remover_linha = tabela_remove.rows[linha._index]._element
                            remover_linha.getparent().remove(remover_linha)

                        else:
                            substituir_trecho_tabela(celula, f'#{i}E_MAIL', info_ad[f'cliente{i}']['email'])

                    if f'#{i}ENDEREÇO' in celula.text:
                        if info_ad[f'cliente{i}']['logradouro'] == 'None':
                            tabela_remove = documento.tables[tabela_index]
                            remover_linha = tabela_remove.rows[linha._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, f'#{i}ENDEREÇO', info_ad[f'cliente{i}']['logradouro'])

                    if f'#{i}CEP' in celula.text:
                        if info_ad[f'cliente{i}']['cep'] == 'None':
                            tabela_remove = documento.tables[tabela_index]
                            remover_linha = tabela_remove.rows[linha._index]._element
                            remover_linha.getparent().remove(remover_linha)
                        else:
                            substituir_trecho_tabela(celula, f'#{i}CEP', info_ad[f'cliente{i}']['cep'])

                #Dados Imovel
                if '#END_IMOVEL' in celula.text:
                    substituir_trecho_tabela(celula, '#END_IMOVEL', dados_imovel['logradouro'] + ', ' + dados_imovel['numero'] + ', ' + dados_imovel['bairro'] + ', ' + dados_imovel['cidade'] + ', ' + dados_imovel['estado'])
                if '#CEP_IMOVEL' in celula.text:
                    if dados_imovel['cep'] == None:
                        tabela_remove = documento.tables[tabela_index]
                        remover_linha = tabela_remove.rows[linha._index]._element
                        remover_linha.getparent().remove(remover_linha)
                    else:
                        substituir_trecho_tabela(celula, '#CEP_IMOVEL', dados_imovel['cep'])

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

                if '#HIDROMETRO' == celula.text:
                    if info_ad['agua'] == '':
                        tabela_para_remover = documento.tables[tabela_index]
                        remover_linha = tabela_para_remover.rows[linha._index]._element
                        remover_linha.getparent().remove(remover_linha)
                    else:
                        substituir_trecho_tabela(celula, '#HIDROMETRO', info_ad['agua'])

    for paragrafo in documento.paragraphs:
        texto = paragrafo.text

        if '#CAPTADOR' in texto:
            substituir_texto(paragrafo, '#CAPTADOR', dados_corretor['nome'])

        if '#CAPTA_CPF' in texto:
            substituir_texto(paragrafo, '#CAPTA_CPF', dados_corretor['cpf_cnpj'])
        if '#FORO' in texto:
            substituir_texto(paragrafo, '#FORO', dados_imovel['cidade'])
    
    download.emit(documento)
    '''except Exception as e:
        error.emit('Erro ao gerar o documento: ' + str(e))'''

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

def inserir_tabelas(documento, tabela, dados_cliente2):

    if dados_cliente2:
        tabela_existente = tabela
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

        tabela_cliente2.rows[0].cells[1].text = '#1PARTE_CLIENTE'
        tabela_cliente2.rows[1].cells[1].text = '#1NACIONALIDADE'
        tabela_cliente2.rows[2].cells[1].text = '#1ESTADO CIVIL'
        tabela_cliente2.rows[3].cells[1].text = '#1CPF'
        tabela_cliente2.rows[4].cells[1].text = '#1E_MAIL'
        tabela_cliente2.rows[5].cells[1].text = '#1ENDEREÇO'
        tabela_cliente2.rows[6].cells[1].text = '#1CEP'

        elemento_tabela_vazia.addnext(tabela_cliente2._element)
        tabela_cliente2.style = tabela_existente.style

        total_tabelas = len(documento.tables)
        tabela_assinatura = documento.tables[total_tabelas - 1]
        elemento_tabela_assinatura = tabela_assinatura._element

        tabela_assinatura_new_cliente = documento.add_table(rows=1, cols=2)

        elemento_tabela_assinatura_new_cliente = tabela_assinatura_new_cliente._element
        tabela_assinatura_new_cliente.rows[0].cells[0].text = '\n_______________________________\n#1PARTE_CLIENTE\nPARTE CONTRATANTE'
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
