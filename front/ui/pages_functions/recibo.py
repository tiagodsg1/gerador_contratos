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

        self.ui.comboBox.addItems(self.clientes)
        self.ui.comboBox_4.addItems(self.clientes)
        self.ui.comboBox_3.addItems(self.corretor)
        
        

    def get_dados(self):
        self.cliente0 = self.ui.comboBox.currentText()
        self.cliente1 = self.ui.comboBox_4.currentText()
        self.corretor = self.ui.comboBox_3.currentText()
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
            self.ui.checkBox_8: 'Outros',
        }

        for checkbox, tipo in tipos.items():
            if checkbox.isChecked():
                tipo_pag = tipo
                if tipo == 'Outros':
                    tipo_pag = self.ui.lineEdit_3.text()
                
        info_ad = {
            'cliente0': self.cliente0,
            'cliente1': self.cliente1,
            'cliente2': None,
            'cliente3': None,
            'mot_pag': mot_pag,
            'quant_pag': quant_pag,
            'data_pag': data_pag,
            'tipo_pag': tipo_pag,
        }
        return self.corretor, info_ad


    
