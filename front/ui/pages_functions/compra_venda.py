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

        self.ui.pushButton.clicked.connect(self.cliente2)
        self.ui.pushButton_2.clicked.connect(self.cliente3)

    def insert_dados(self, comprador, vendedor, corretor):
        self.comprador = comprador
        self.vendedor = vendedor
        self.corretor = corretor
        self.hide_all()
        self.hide_combobox()
        self.ui.comboBox.addItems(self.vendedor)
        self.ui.comboBox_2.addItems(self.comprador)
        self.ui.comboBox_3.addItems(self.corretor)
    
    def hide_all(self):

        for line_edit in self.checkbox_lineedit_map.values():
            line_edit.hide()

    def hide_combobox(self):
        self.ui.comboBox_4.hide()
        self.ui.comboBox_5.hide()

    def cliente2(self):
        self.ui.comboBox_4.show()
        self.ui.comboBox_4.addItems(self.vendedor)
        self.ui.pushButton.hide()
        self.cliente_2 = True

    def cliente3(self):
        self.ui.comboBox_5.show()
        self.ui.comboBox_5.addItems(self.comprador)
        self.ui.pushButton_2.hide()
        self.cliente_3 = True

    def get_dados(self):
        lista_comprador_vendedor = []
        if self.cliente_2:
            self.cliente_2 = self.ui.comboBox_4.currentText()
        if self.cliente_3:
            self.cliente_3 = self.ui.comboBox_5.currentText()

        self.vendedor = self.ui.comboBox.currentText()
        self.comprador = self.ui.comboBox_2.currentText()
        self.corretor = self.ui.comboBox_3.currentText()
        
        return self.comprador, self.vendedor, self.corretor, self.cliente_2, self.cliente_3
    
