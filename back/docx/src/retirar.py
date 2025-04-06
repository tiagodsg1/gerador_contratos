
from docx.enum.text import WD_COLOR_INDEX


def retirar(paragrafo): 
    for run in paragrafo.runs:
        if run.font.highlight_color == WD_COLOR_INDEX.YELLOW:
            run.font.highlight_color = None


def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    paragraph._p = paragraph._element = None  # desvincula o parágrafo do Python