
from docx.enum.text import WD_COLOR_INDEX

def retirar(paragrafo): 
    for run in paragrafo.runs:
        if run.font.highlight_color == WD_COLOR_INDEX.YELLOW:
            run.font.highlight_color = None

def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    paragraph._p = paragraph._element = None  # desvincula o parágrafo do Python


def substituir_texto(paragraph, marcador, novo_valor):
    for run in paragraph.runs:
        if marcador in run.text:
            run.text = run.text.replace(marcador, novo_valor)

def remover_trecho(paragraph, trecho):
    for run in paragraph.runs:
        if trecho in run.text:
            run.text = run.text.replace(trecho, '')

def substituir_trecho_tabela(cell, marcador, novo_valor):
    for paragrafo in cell.paragraphs:
        texto_completo = ''.join(run.text for run in paragrafo.runs)
        if marcador in texto_completo:
            novo_texto = texto_completo.replace(marcador, novo_valor)
            # Limpa todos os runs existentes
            for run in paragrafo.runs:
                run.text = ''
            # Coloca o texto de volta no primeiro run
            if paragrafo.runs:
                paragrafo.runs[0].text = novo_texto