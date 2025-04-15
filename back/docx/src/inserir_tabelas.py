from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt
from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn


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
        tabela_assinatura_new_cliente.rows[0].cells[0].text = '\n_____________________________________________________\n#1PARTE_CLIENTE\nPARTE CONTRATANTE'
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
