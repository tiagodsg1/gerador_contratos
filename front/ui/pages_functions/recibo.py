from front.ui.pages.recibo_pagamento.recibo_pagamento import Ui_Form
from PyQt5.QtWidgets import QWidget

class recibo(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.checkbox_lineedit_map = {
            self.ui.checkBox_2: self.ui.widget_pagamento,
            self.ui.checkBox_8: self.ui.lineEdit_3,
        }

        for checkbox, widget in self.checkbox_lineedit_map.items():
            checkbox.stateChanged.connect(
                lambda state, w=widget: w.setVisible(state == 2)
            )


    def insert_dados(self, corretor, clientes):
        self.corretor = corretor
        self.clientes = clientes
        self.ui.comboBox_3.addItems(self.corretor)
        self.ui.comboBox_4.addItems(self.clientes)
        self.ui.comboBox_5.addItems(self.clientes)

    def get_dados(self):
        self.corretor = self.ui.comboBox_3.currentText()
        self.recebedor = self.ui.comboBox_4.currentText()
        self.pagador = self.ui.comboBox_5.currentText()
        mot_pag = self.ui.lineEdit.text()
        quant_pag = self.ui.lineEdit_2.text()
        data_pag = self.ui.dateEdit.text()
        
        tipo_pag = None
        tipos = {
            self.ui.checkBox_3: 'Pix',
            self.ui.checkBox_4: 'Boleto',
            self.ui.checkBox_5: 'Transferência Bancária',
            self.ui.checkBox_6: 'Dinheiro',
            self.ui.checkBox_7: 'Cartão',
        }

        for checkbox, tipo in tipos.items():
            if checkbox.isChecked():
                tipo_pag = tipo
                

        return self.corretor, tipo_pag, mot_pag, quant_pag, self.recebedor, self.pagador, data_pag


    
