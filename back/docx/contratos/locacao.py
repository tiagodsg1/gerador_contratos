from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Cm
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt

from back.docx.inserir_tabelas import inserir_tabelas

def locacao():
    '''Função para gerar o contrato de locação'''

