from PyQt5.QtWidgets import QWidget
from front.ui.pages.administracao_locacao.administracao_locacao import Ui_Form
import time

class administracao_locacao(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.radioButton_2.clicked.connect(self.radio_button_clicked)

    def insert_dados(self, clientes, corretor, error):
        self.cliente = clientes
        self.corretor = corretor
        self.error = error
        self.ui.comboBox_2.addItems(self.cliente)
        self.ui.comboBox_5.addItems(self.cliente)

        self.ui.comboBox_3.addItems(self.corretor)

    def radio_button_clicked(self):
        if self.ui.radioButton_2.isChecked():
            self.ui.comboBox_5.setEnabled(True)
        else:
            self.ui.comboBox_5.setEnabled(False)

    def get_dados(self):

        self.cliente = self.ui.comboBox_2.currentText()
        self.corretor = self.ui.comboBox_3.currentText()
        porcentagem = self.ui.lineEdit.text()

        if porcentagem == '':
            self.ui.lineEdit.setStyleSheet("border-color: red;")
            self.error('Campo de Porcentagem não pode ficar vazio')
            return None, None
        
        cartorio = self.ui.lineEdit_8.text()
        n_iptu = self.ui.lineEdit_9.text()
        relogio = self.ui.lineEdit_10.text()
        monobitrifasico = self.ui.lineEdit_13.text()
        agua = self.ui.lineEdit_16.text()
        gas = self.ui.lineEdit_14.text()
        funesbom = self.ui.lineEdit_15.text()
        matricula = self.ui.lineEdit_11.text()
        luz = self.ui.lineEdit_12.text()

        info_ad = {
            'cliente0': self.cliente,
            'cliente1': None,
            'cliente2': None,
            'cliente3': None,
            'porcentagem': porcentagem,
            'cartorio' : cartorio,
            'n_iptu': n_iptu,
            'relogio': relogio,
            'monobitrifasico': monobitrifasico,
            'agua': agua,
            'luz': luz,
            'gas': gas,
            'funesbom': funesbom,
            'matricula': matricula,
        }

        if self.ui.radioButton_2.isChecked():
            self.cliente_2 = self.ui.comboBox_5.currentText()
            info_ad['cliente1'] = self.cliente_2
            
        return self.corretor, info_ad