from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
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

        tabela_locador2 = documento.add_table(rows=7, cols=2)

        column_widths = [Cm(9.25), Cm(20)]  # Defina a largura de cada coluna

        for col_index, width in enumerate(column_widths):
            for cell in tabela_locador2.columns[col_index].cells:
                cell.width = width

        tabela_locador2.rows[0].cells[0].text = 'Nome'
        tabela_locador2.rows[1].cells[0].text = 'Nacionalidade'
        tabela_locador2.rows[2].cells[0].text = 'Estado Civil'
        tabela_locador2.rows[3].cells[0].text = 'CPF'
        tabela_locador2.rows[4].cells[0].text = 'E-mail'
        tabela_locador2.rows[5].cells[0].text = 'Endereço'
        tabela_locador2.rows[6].cells[0].text = 'CEP'

        tabela_locador2.rows[0].cells[1].text = '#1PARTE_CLIENTE'
        tabela_locador2.rows[1].cells[1].text = '#1NACIONALIDADE'
        tabela_locador2.rows[2].cells[1].text = '#1ESTADO CIVIL'
        tabela_locador2.rows[3].cells[1].text = '#1CPF'
        tabela_locador2.rows[4].cells[1].text = '#1E_MAIL'
        tabela_locador2.rows[5].cells[1].text = '#1ENDERECO'
        tabela_locador2.rows[6].cells[1].text = '#1CEP'

        elemento_tabela_vazia.addnext(tabela_locador2._element)
        tabela_locador2.style = tabela_existente.style

        total_tabelas = len(documento.tables)
        tabela_assinatura = documento.tables[total_tabelas - 1]
        elemento_tabela_assinatura = tabela_assinatura._element

        tabela_assinatura_new_cliente = documento.add_table(rows=1, cols=2)

        elemento_tabela_assinatura_new_cliente = tabela_assinatura_new_cliente._element
        tabela_assinatura_new_cliente.rows[0].cells[0].text = '\n\n\n\n\n______________________________________\n#2PARTE_CLIENTE_ASSINATURA\nPARTE CONTRATANTE'
        for i in range(2):
            for paragraph in tabela_assinatura_new_cliente.rows[0].cells[i].paragraphs:
                paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

        elemento_tabela_assinatura.addnext(elemento_tabela_assinatura_new_cliente)
        add_table_borders(tabela_locador2)
