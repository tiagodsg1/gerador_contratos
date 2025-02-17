from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox, QWidget
from front.ui.pages.administracao_locacao.administracao_locacao import Ui_Form

class administracao_locacao(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.clientes = None
        self.cliente_2 = False
        self.cliente_3 = False
        self.ui.pushButton.clicked.connect(self.cliente2)
        self.ui.pushButton_3.clicked.connect(self.cliente3)

    def insert_dados(self, clientes):
        self.clientes = clientes
        self.hiden()
        self.ui.comboBox.addItems(self.clientes)
        self.cliente = self.ui.comboBox.currentText()

    def cliente2(self):
        self.ui.pushButton.hide()
        self.ui.comboBox_2.show()
        self.ui.label_3.show()
        self.ui.comboBox_2.addItems(self.clientes)
        self.cliente_2 = True

    def cliente3(self):
        self.ui.pushButton_3.hide()
        self.ui.comboBox_3.show()
        self.ui.label_4.show()
        self.ui.comboBox_3.addItems(self.clientes)
        self.cliente_3 = True
    
    def hiden(self):
        self.ui.comboBox_2.hide()
        self.ui.label_3.hide()
        self.ui.comboBox_3.hide()
        self.ui.label_4.hide()

    def get_dados(self):
        if self.cliente_2 == True:
            self.cliente_2 = self.ui.comboBox_2.currentText()
        if self.cliente_3 == True:
            self.cliente_3 = self.ui.comboBox_3.currentText()
        return self.ui.lineEdit.text(), self.cliente, self.cliente_2, self.cliente_3