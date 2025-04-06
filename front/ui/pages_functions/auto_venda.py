from front.ui.pages.auto_venda.autorizacao import Ui_Form
from PyQt5.QtWidgets import QWidget

class autorizacao(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.cliente_2 = False
        self.cliente_3 = False
        self.ui.pushButton_3.clicked.connect(self.cliente2)
        self.ui.pushButton_4.clicked.connect(self.cliente3)
    
    def insert_dados(self, clientes, corretor):
        self.clientes = clientes
        self.corretor = corretor
        self.hiden()
        self.ui.comboBox.addItems(self.corretor)
        self.ui.comboBox_2.addItems(self.clientes)

    def cliente2(self):
        self.ui.pushButton_3.hide()
        self.ui.comboBox_3.show()
        self.ui.label_4.show()
        self.ui.comboBox_3.addItems(self.clientes)
        self.cliente_2 = True

    def cliente3(self):
        self.ui.pushButton_4.hide()
        self.ui.comboBox_4.show()
        self.ui.label_5.show()
        self.ui.comboBox_4.addItems(self.clientes)
        self.cliente_3 = True

    def hiden(self):
        self.ui.comboBox_3.hide()
        self.ui.label_4.hide()
        self.ui.comboBox_4.hide()
        self.ui.label_5.hide()

    def get_dados(self):

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
        if self.cliente_2 == True:
            self.cliente_2 = self.ui.comboBox_3.currentText()
        if self.cliente_3 == True:
            self.cliente_3 = self.ui.comboBox_4.currentText()

        self.cliente = self.ui.comboBox_2.currentText()
        self.corretor = self.ui.comboBox.currentText()
        
        return self.cliente, self.corretor , self.cliente_2, self.cliente_3, info_ad
