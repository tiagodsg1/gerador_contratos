from front.ui.pages.auto_venda.autorizacao import Ui_Form
from PyQt5.QtWidgets import QWidget

class autorizacao(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.radioButton_2.clicked.connect(self.radio_button)
    
    def insert_dados(self, clientes, corretor):
        self.clientes = clientes
        self.corretor = corretor
        self.ui.comboBox_2.addItems(self.clientes)
        self.ui.comboBox_5.addItems(self.clientes)
        self.ui.comboBox_3.addItems(self.corretor)

    def radio_button(self):
        if self.ui.radioButton_2.isChecked():
            self.ui.comboBox_5.setEnabled(True)
        else:
            self.ui.comboBox_5.setEnabled(False)


    def get_dados(self):
        
        cliente0 = self.ui.comboBox_2.currentText()
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
            'cliente0': cliente0,
            'cliente1': None,
            'cliente2': None,
            'cliente3': None,
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
            info_ad['cliente1'] = self.ui.comboBox_5.currentText()

        self.corretor = self.ui.comboBox_3.currentText()
        
        return self.corretor, info_ad
