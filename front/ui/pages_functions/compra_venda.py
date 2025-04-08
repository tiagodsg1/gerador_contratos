from front.ui.pages.compra_venda.compra_venda import Ui_Form
from PyQt5.QtWidgets import QWidget

class compra_venda(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.cliente_2 = False
        self.cliente_3 = False
        self.checkbox_lineedit_map = {
            self.ui.checkBox: self.ui.lineEdit,
            self.ui.checkBox_2: self.ui.lineEdit_2,
            self.ui.checkBox_3: self.ui.lineEdit_3,
            self.ui.checkBox_4: self.ui.lineEdit_4,
            self.ui.checkBox_5: self.ui.lineEdit_5,
            self.ui.checkBox_6: self.ui.lineEdit_6,
        }
        for checkbox, line_edit in self.checkbox_lineedit_map.items():
            checkbox.stateChanged.connect(
                lambda state, le=line_edit: le.setVisible(state == 2)
            )

        self.ui.radioButton.clicked.connect(self.radio_button_clicked)
        self.ui.radioButton_2.clicked.connect(self.radio_button_clicked)

    def insert_dados(self, comprador, vendedor, corretor):
        self.comprador = comprador
        self.vendedor = vendedor
        self.corretor = corretor
        self.ui.comboBox.addItems(self.vendedor)
        self.ui.comboBox_4.addItems(self.vendedor)

        self.ui.comboBox_2.addItems(self.comprador)
        self.ui.comboBox_5.addItems(self.comprador)

        self.ui.comboBox_3.addItems(self.corretor)

    def radio_button_clicked(self):
        if self.ui.radioButton.isChecked():
            self.ui.comboBox_4.setEnabled(True)
        else:
            self.ui.comboBox_4.setEnabled(False)

        if self.ui.radioButton_2.isChecked():
            self.ui.comboBox_5.setEnabled(True)
        else:
            self.ui.comboBox_5.setEnabled(False)        

    def get_dados(self):

        cartorio = self.ui.lineEdit_9.text()
        n_iptu = self.ui.lineEdit_10.text()
        matricula = self.ui.lineEdit_11.text()
        valor = self.ui.lineEdit.text()
        sinal = self.ui.lineEdit_2.text()
        entrada = self.ui.lineEdit_3.text()
        financiamento = self.ui.lineEdit_4.text()
        fgts = self.ui.lineEdit_5.text()
        subsidio = self.ui.lineEdit_6.text()
        isencao = self.ui.lineEdit_7.text()
        prazo = self.ui.lineEdit_8.text()
        posse = self.ui.textEdit.toPlainText()

        info_ad = {
            'cartorio': cartorio,
            'n_iptu': n_iptu,
            'matricula': matricula,
            'valor': valor,
            'sinal': sinal,
            'entrada': entrada,
            'financiamento': financiamento,
            'fgts': fgts,
            'subsidio': subsidio,
            'isencao': isencao,
            'prazo': prazo,
            'posse': posse,
            'escritura': False
        }

        if self.ui.radioButton.isChecked():
            self.cliente_2 = self.ui.comboBox_4.currentText()

        if self.ui.radioButton_2.isChecked():
            self.cliente_3 = self.ui.comboBox_5.currentText()

        if self.ui.checkBox_16.isChecked():
            info_ad['escritura'] = True

        self.vendedor = self.ui.comboBox.currentText()
        self.comprador = self.ui.comboBox_2.currentText()
        self.corretor = self.ui.comboBox_3.currentText()
        
        return self.comprador, self.vendedor, self.corretor, self.cliente_2, self.cliente_3, info_ad