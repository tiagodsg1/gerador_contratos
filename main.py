from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QFileDialog
import os

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
from front.ui.pages_functions.area import Area

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
    finished = pyqtSignal(str)
    download_docx = pyqtSignal(object)

    def __init__(self):
        super().__init__()
        self.t_contrato = None
        self.imovel = None
        self.corretor = None
        self.comprador = None
        self.vendedor = None
        self.tipo = None
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
        self.info_ad = None

    def run(self):
        if self.t_contrato != 'Recibo de Pagamento':
            dados_imovel = GetDados(self.imovel).get_imoveis(self.tipo)
        dados_corretor = GetDados(self.corretor).get_corretores()

        dados_cliente2 = None
        dados_cliente3 = None

        try:

            self.cliente = self.info_ad['cliente0']
            self.cliente2 = self.info_ad['cliente1']
        
            if self.cliente:
                dados_cliente = GetDados(self.cliente).get_clientes()
                self.info_ad['cliente0'] = dados_cliente

            if self.cliente2:
                dados_cliente2 = GetDados(self.cliente2).get_clientes()
                self.info_ad['cliente1'] = dados_cliente2

        except Exception as e:
            self.error.emit(f'Erro ao buscar dados: {str(e)}\nVerifique se os clientes estão cadastrados ou se os dados estão corretos.\nCaso não esteja cadastrado, cadastre o cliente antes de gerar o contrato.')
            return
        
        try:
            if self.t_contrato == 'Administração de Locação':
                base_dir = os.path.dirname(os.path.abspath(__file__))
                caminho_docx = os.path.join(base_dir, 'Contratos_docx', 'Administração de Locação.docx')

                self.dicionario = {
                                'imovel': dados_imovel, 
                                'corretor': dados_corretor,
                                'info_ad': self.info_ad,
                                'sucesso':self.sucesso, 
                                'error':self.error, 
                                'download': self.download_docx}            
                self.contrato = GerarDocx(self.t_contrato, caminho_docx, self.dicionario)

            if self.t_contrato == 'Autorização de Venda':
                base_dir = os.path.dirname(os.path.abspath(__file__))
                caminho_docx = os.path.join(base_dir, 'Contratos_docx', 'Autorização de Venda.docx')
                self.dicionario = {'cliente': dados_cliente,
                                'corretor': dados_corretor,
                                    'imovel': dados_imovel,
                                    'cliente2': dados_cliente2,
                                    'cliente3': dados_cliente3,
                                    'info_ad': self.info_ad,
                                    'sucesso': self.sucesso,
                                    'error': self.error,
                                    'download': self.download_docx}
                self.contrato = GerarDocx(self.t_contrato, caminho_docx, self.dicionario)

            '''if self.t_contrato == 'Compromisso de Compra e Venda':
                base_dir = os.path.dirname(os.path.abspath(__file__))
                caminho_docx = os.path.join(base_dir, 'Contratos_docx', 'Compromisso de Compra e Venda.docx')
                self.dicionario = {'comprador': dados_comprador,
                                'imovel': dados_imovel,
                                    'vendedor': dados_vendedor,
                                    'corretor': dados_corretor,
                                    'cliente2': dados_cliente2,
                                    'cliente3': dados_cliente3,
                                    'sucesso': self.sucesso,
                                    'info_ad': self.info_ad,
                                    'error': self.error,
                                    'download': self.download_docx}
                self.contrato = GerarDocx(self.t_contrato, caminho_docx, self.dicionario)'''

            if self.t_contrato == 'Locação':
                base_dir = os.path.dirname(os.path.abspath(__file__))
                caminho_docx = os.path.join(base_dir, 'Contratos_docx', 'Locação Residencial.docx')
                self.dicionario = {
                                'corretor': dados_corretor,
                                'imovel': dados_imovel,
                                'info_ad': self.info_ad,
                                'sucesso': self.sucesso,
                                'error': self.error,
                                'download': self.download_docx}
                self.contrato = GerarDocx(self.t_contrato, caminho_docx, self.dicionario)

            if self.t_contrato == 'Recibo de Pagamento':
                base_dir = os.path.dirname(os.path.abspath(__file__))
                caminho_docx = os.path.join(base_dir, 'Contratos_docx', 'Recibo de Pagamento.docx')
                self.dicionario = {'corretor': dados_corretor,
                                'pagador': dados_cliente,
                                'recebedor': dados_cliente2,
                                'tipo_pag': self.tipo_pag,
                                'quant_pag': self.quant_pag,
                                'mot_pag': self.mot_pag,
                                'data_pag': self.data_pag,
                                'sucesso': self.sucesso,
                                'error': self.error,
                                'download': self.download_docx}
                self.contrato = GerarDocx(self.t_contrato, caminho_docx, self.dicionario)

            if self.t_contrato == 'Consultoria':
                if self.min_valor == None:
                    self.min_valor = dados_imovel['valor']

                if self.av_valor == None:
                    self.av_valor = dados_imovel['valor']

                self.dicionario = {'corretor': dados_corretor,
                                'cliente': dados_cliente,
                                'imovel': dados_imovel,
                                'min_valor': self.min_valor,
                                'av_valor': self.av_valor,
                                'pro_valor': self.pro_valor,
                                'cons_valor': self.cons_valor,
                                'sucesso': self.sucesso,
                                'error': self.error,
                                'download': self.download_docx}
                
                self.contrato = GerarDocx(self.t_contrato, "./Contratos_docx/Consultoria.docx", self.dicionario)
        except Exception as e:
            self.error.emit(f'Erro ao gerar o contrato: {str(e)}\nVerifique se os dados estão corretos.')
            return    
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
        self.ui.pushButton_3.clicked.connect(self.adicionar_endereco)
        self.ui.pushButton_4.clicked.connect(self.area)
        self.ui.pushButton_5.clicked.connect(self.chamar_variavel)
        self.ui.pushButton_6.clicked.connect(self.download_table)

    def click(self):
        self.worker.t_contrato = self.ui.comboBox.currentText()
        item = self.ui.comboBox_2.currentText()
        item = item.split(',')[0]
        if item == '' or item == None:
            QMessageBox.warning(self, 'Erro', 'Selecione um imóvel')
            return
        self.worker.imovel = item
        self.worker.sucesso.connect(self.download_sucesso)
        self.worker.error.connect(self.download_error)
        self.worker.download_docx.connect(self.download_docx)


        if self.ui.comboBox.currentText() == 'Administração de Locação':
            self.worker.corretor, self.worker.info_ad = self.administracao_locacao.get_dados()
            if self.worker.corretor == None:
               return

        if self.ui.comboBox.currentText() == 'Autorização de Venda':
            self.worker.corretor, self.worker.cliente2, self.worker.cliente3, self.worker.info_ad = self.autorizacao.get_dados()
        
        if self.ui.comboBox.currentText() == 'Compromisso de Compra e Venda':
            self.worker.comprador, self.worker.vendedor, self.worker.corretor, self.worker.cliente2, self.worker.cliente3, self.worker.info_ad = self.compra_venda.get_dados()

        if self.ui.comboBox.currentText() == 'Locação':
            self.worker.cliente, self.worker.cliente2, self.worker.corretor, self.worker.info_ad = self.locacao.get_dados()
            if self.worker.cliente == None:
                return

        if self.ui.comboBox.currentText() == 'Recibo de Pagamento':
            self.worker.corretor, self.worker.tipo_pag, self.worker.mot_pag, self.worker.quant_pag, self.worker.cliente, self.worker.cliente2, self.worker.data_pag = self.recibo.get_dados()

        if self.ui.comboBox.currentText() == 'Consultoria':
            self.worker.corretor, self.worker.min_valor, self.worker.av_valor, self.worker.pro_valor, self.worker.cons_valor, self.worker.cliente = self.consultoria.get_dados()

        
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
            self.administracao_locacao.insert_dados(self.cliente_lista, self.corretor_lista, self.download_error)
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
            self.locacao.insert_dados(self.cliente_lista, self.corretor_lista, self.download_error)
            self.locacao.setParent(self.ui.frame_3)
            self.locacao.show()

        if self.ui.comboBox.currentText() == 'Recibo de Pagamento':
            self.clear_frame(self.ui.frame_3)
            self.recibo.insert_dados(self.corretor_lista, self.cliente_lista)
            self.recibo.setParent(self.ui.frame_3)
            self.recibo.show()

        if self.ui.comboBox.currentText() == 'Consultoria':
            self.clear_frame(self.ui.frame_3)
            self.consultoria.insert_dados(self.corretor_lista, self.cliente_lista)
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
    
    def download_docx(self, documento):
        file_name, _ = QFileDialog.getSaveFileName(None, "Save Document", "", "Word Document (*.docx)")
        if file_name:
            documento.save(file_name)
            QMessageBox.information(self, 'Sucesso', 'Documento salvo com sucesso!')

    def adicionar_endereco(self):
        self.tipo = self.ui.comboBox_5.currentText()
        item = self.ui.comboBox_2.currentText()
        item = item.split(',')[0]
        if item == '' or item == None:
            QMessageBox.warning(self, 'Erro', 'Selecione um imóvel')
            return
        try:
            imovel_select = GetDados(item).get_imoveis(self.tipo)
            self.ui.label_2.setText(f"Endereço : {imovel_select['logradouro']}, {imovel_select['numero']}, {imovel_select['bairro']}, {imovel_select['cidade']}, Rio de Janeiro")
            self.ui.label_2.setWordWrap(True)
        except Exception as e:
            QMessageBox.warning(self, 'Erro', f'Erro ao buscar endereço: {str(e)}\nVerifique se o imóvel está cadastrado ou se os dados estão corretos.')
            return

    def area(self):
        self.area_contratos = Area()
        self.area_contratos.dados_corretor(self.corretor_lista)
        self.area_contratos.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()