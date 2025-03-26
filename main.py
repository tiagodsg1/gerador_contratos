from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import QThread, pyqtSignal

from front.ui.Main import Ui_MainWindow

from back.bd.nomes import GetNomes
from back.bd.dados import GetDados
from back.bd.update.download import Dados

from back.docx.gerar_docx import GerarDocx

from front.ui.pages_functions.administracao_locacao import administracao_locacao
from front.ui.pages_functions.auto_venda import autorizacao
from front.ui.pages_functions.compra_venda import compra_venda
from front.ui.pages_functions.locacao import locacao
from front.ui.pages_functions.recibo import recibo
from front.ui.pages_functions.consultoria import consultoria

class WorkerDownload(QThread):
    sucesso = pyqtSignal(str)
    error = pyqtSignal(str)
    finished = pyqtSignal()
    
    def __init__(self):
        super().__init__()

    def run(self):
        Dados(self.sucesso, self.error, self.finished)

class Worker(QThread):

    sucesso = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.t_contrato = None
        self.imovel = None
        self.cliente = None
        self.corretor = None
        self.comprador = None
        self.vendedor = None
        self.tipo = None
        self.cliente2 = None
        self.cliente3 = None
        self.percentual = None
        self.download = None
        self.corretor = None
        self.tipo_pag = None
        self.min_valor = None
        self.av_valor = None
        self.pro_valor = None
        self.cons_valor = None
        self.mot_pag = None
        self.quant_pag = None
        self.data_pag = None

    def run(self):
        if self.t_contrato != 'Recibo de Pagamento':
            dados_imovel = GetDados(self.imovel).get_imoveis(self.tipo)
        dados_corretor = GetDados(self.corretor).get_corretores()
        dados_cliente2 = None
        dados_cliente3 = None
        
        if self.cliente:
            dados_cliente = GetDados(self.cliente).get_clientes()

        if self.cliente2:
            dados_cliente2 = GetDados(self.cliente2).get_clientes()

        if self.cliente3:
            dados_cliente3 = GetDados(self.cliente3).get_clientes()
            
        if self.comprador:
            dados_comprador = GetDados(self.comprador).get_clientes()
            dados_vendedor = GetDados(self.vendedor).get_clientes()
        
        if self.t_contrato == 'Administração de Locação':

            self.dicionario = {'cliente' : dados_cliente, 
                               'imovel': dados_imovel, 
                               'cliente2': dados_cliente2, 
                               'cliente3': dados_cliente3, 
                               'sucesso':self.sucesso, 
                               'error':self.error, 
                               'percentual':self.percentual}
            
            self.contrato = GerarDocx(self.t_contrato, "./Contratos/Contrato de Administração de Locação.docx", self.dicionario)

        if self.t_contrato == 'Autorização de Venda':
            self.dicionario = {'cliente': dados_cliente,
                               'corretor': dados_corretor,
                                'imovel': dados_imovel,
                                'cliente2': dados_cliente2,
                                'cliente3': dados_cliente3,
                                'sucesso': self.sucesso,
                                'error': self.error}
            self.contrato = GerarDocx(self.t_contrato, "./Contratos/Autorização de Venda.docx", self.dicionario)

        if self.t_contrato == 'Compromisso de Compra e Venda':
            self.dicionario = {'comprador': dados_comprador,
                                'vendedor': dados_vendedor,
                                'corretor': dados_corretor,
                                'cliente2': dados_cliente2,
                                'cliente3': dados_cliente3,
                                'sucesso': self.sucesso,
                                'error': self.error}
            self.contrato = GerarDocx(self.t_contrato, "./Contratos/Compromisso de Compra e Venda.docx", self.dicionario)

        if self.t_contrato == 'Locação':
            self.dicionario = {'cliente': dados_cliente,
                               'corretor': dados_corretor,
                               'imovel': dados_imovel,
                               'sucesso': self.sucesso,
                               'error': self.error}
            self.contrato = GerarDocx(self.t_contrato, "./Contratos/Contrato de Locação.docx", self.dicionario)

        if self.t_contrato == 'Recibo de Pagamento':
            self.dicionario = {'corretor': dados_corretor,
                               'pagador': dados_cliente,
                               'recebedor': dados_cliente2,
                               'tipo_pag': self.tipo_pag,
                               'quant_pag': self.quant_pag,
                               'mot_pag': self.mot_pag,
                               'data_pag': self.data_pag,
                               'sucesso': self.sucesso,
                               'error': self.error}
            self.contrato = GerarDocx(self.t_contrato, "./Contratos/Recibo de Pagamento.docx", self.dicionario)

        if self.t_contrato == 'Consultoria':
            self.dicionario = {'corretor': dados_corretor,
                               'sucesso': self.sucesso,
                               'error': self.error}
            self.contrato = GerarDocx(self.t_contrato, "./Contratos/Consultoria.docx", self.dicionario)
            
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.esconder()
        self.worker = Worker()
        self.worker_download = WorkerDownload()
        self.bd = GetNomes()

        self.administracao_locacao = administracao_locacao()
        self.autorizacao = autorizacao()
        self.compra_venda = compra_venda()
        self.locacao = locacao()
        self.recibo = recibo()
        self.consultoria = consultoria()

        self.tipo = None

        self.ui.pushButton.clicked.connect(self.click)
        
        self.cliente_lista = [cliente[0] for cliente in self.bd.get_clientes()]
        self.cliente_lista.sort()

        self.corretor_lista = [corretor[0] for corretor in self.bd.get_corretores()]
        self.corretor_lista.sort()
        
        self.ui.pushButton_2.clicked.connect(self.buscar_imovel)
        self.ui.pushButton_5.clicked.connect(self.chamar_variavel)
        self.ui.pushButton_6.clicked.connect(self.download_table)

    def click(self):
        self.worker.t_contrato = self.ui.comboBox.currentText()
        item = self.ui.comboBox_2.currentText()
        item = item.split(',')[0]
        self.worker.imovel = item
        self.worker.sucesso.connect(self.download_sucesso)
        self.worker.error.connect(self.download_error)

        if self.ui.comboBox.currentText() == 'Administração de Locação':
            self.worker.percentual, self.worker.cliente, self.worker.cliente2, self.worker.cliente3 = self.administracao_locacao.get_dados()

        if self.ui.comboBox.currentText() == 'Autorização de Venda':
            self.worker.cliente, self.worker.corretor, self.worker.cliente2, self.worker.cliente3 = self.autorizacao.get_dados()
        
        if self.ui.comboBox.currentText() == 'Compromisso de Compra e Venda':
            self.worker.comprador, self.worker.vendedor, self.worker.corretor, self.worker.cliente2, self.worker.cliente3 = self.compra_venda.get_dados()

        if self.ui.comboBox.currentText() == 'Locação':
            self.worker.cliente, self.worker.corretor, self.worker.cliente2 = self.locacao.get_dados()

        if self.ui.comboBox.currentText() == 'Recibo de Pagamento':
            self.worker.corretor, self.worker.tipo_pag, self.worker.mot_pag, self.worker.quant_pag, self.worker.cliente, self.worker.cliente2, self.worker.data_pag = self.recibo.get_dados()

        if self.ui.comboBox.currentText() == 'Consultoria':
            self.worker.corretor, self.worker.min_valor, self.worker.av_valor, self.worker.pro_valor, self.cons_valor = self.consultoria.get_dados()

        self.worker.tipo = self.tipo
        self.iniciar()

    def buscar_imovel(self):
        if self.ui.comboBox.currentText() == 'Recibo de Pagamento':
            self.tipo = None
        else:
            self.tipo = self.ui.comboBox_5.currentText()
            if self.tipo == 'Logradouro':
                imovel_lista = [imovel for imovel in self.bd.get_imoveis(self.tipo)]
                self.ui.comboBox_2.clear()
                self.ui.comboBox_2.addItems(imovel_lista)

            else:
                imovel_lista = [imovel[0] for imovel in self.bd.get_imoveis(self.tipo)]
                imovel_lista.sort()
                self.ui.comboBox_2.clear()
                self.ui.comboBox_2.addItems(imovel_lista)

    def esconder(self):
        pass

    def chamar_variavel(self):
        
        if self.ui.comboBox.currentText() == 'Administração de Locação':
            self.clear_frame(self.ui.frame_3)
            self.administracao_locacao.setParent(self.ui.frame_3)
            self.administracao_locacao.insert_dados(self.cliente_lista)
            self.administracao_locacao.show()
        
        if self.ui.comboBox.currentText() == 'Autorização de Venda':
            self.clear_frame(self.ui.frame_3)
            self.autorizacao.insert_dados(self.cliente_lista, self.corretor_lista)
            self.autorizacao.setParent(self.ui.frame_3)
            self.autorizacao.show()

        if self.ui.comboBox.currentText() == 'Compromisso de Compra e Venda':
            self.clear_frame(self.ui.frame_3)
            self.compra_venda.insert_dados(self.cliente_lista, self.cliente_lista, self.corretor_lista)
            self.compra_venda.setParent(self.ui.frame_3)
            self.compra_venda.show()

        if self.ui.comboBox.currentText() == 'Locação':
            self.clear_frame(self.ui.frame_3)
            self.locacao.insert_dados(self.cliente_lista, self.corretor_lista)
            self.locacao.setParent(self.ui.frame_3)
            self.locacao.show()

        if self.ui.comboBox.currentText() == 'Recibo de Pagamento':
            self.clear_frame(self.ui.frame_3)
            self.recibo.insert_dados(self.corretor_lista, self.cliente_lista)
            self.recibo.setParent(self.ui.frame_3)
            self.recibo.show()

        if self.ui.comboBox.currentText() == 'Consultoria':
            self.clear_frame(self.ui.frame_3)
            self.consultoria.insert_dados(self.corretor_lista)
            self.consultoria.setParent(self.ui.frame_3)
            self.consultoria.show()

    def iniciar(self):
        self.worker.start()

    def download_table(self):
        self.ui.pushButton_6.setText('Atualizando...')
        self.ui.pushButton_6.setEnabled(False)
        self.worker_download.sucesso.connect(self.download_sucesso)
        self.worker_download.error.connect(self.download_error)
        self.worker_download.finished.connect(self.download_finished)
        self.worker_download.start()

    def download_sucesso(self, msg):
        QMessageBox.information(self, 'Sucesso', msg)
        

    def download_error(self, msg):
        QMessageBox.warning(self, 'Erro', msg)
    
    def download_finished(self):
        self.ui.pushButton_6.setText('Atualizar database')
        self.ui.pushButton_6.setEnabled(True)

    def clear_frame(self, frame):
        for child in frame.children():
            if isinstance(child, QWidget):
                child.hide()
                
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()