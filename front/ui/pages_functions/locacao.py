from front.ui.pages.locacao.locacao import Ui_Form
from PyQt5.QtWidgets import QWidget

class locacao(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.cliente_2 = False
        self.checkbox_lineedit_map = {
            self.ui.checkBox: self.ui.lineEdit_3,
            self.ui.checkBox_2: self.ui.lineEdit_4,
            self.ui.checkBox_3: self.ui.lineEdit_5,
            self.ui.checkBox_6: self.ui.lineEdit_7,
        }
        for checkbox, line_edit in self.checkbox_lineedit_map.items():
            checkbox.stateChanged.connect(
                lambda state, le=line_edit: le.setVisible(state == 2)
            )

        self.ui.pushButton_2.clicked.connect(self.cliente2)

    def insert_dados(self, locador, corretor):
        self.locador = locador
        self.corretor = corretor
        self.hide_all()
        self.hide_combobox()
        self.ui.comboBox_2.addItems(self.locador)
        self.ui.comboBox_3.addItems(self.corretor)

    def hide_all(self):

        for line_edit in self.checkbox_lineedit_map.values():
            line_edit.hide()

    def hide_combobox(self):
        self.ui.comboBox_5.hide()

    def cliente2(self):
        self.ui.comboBox_5.show()
        self.ui.comboBox_5.addItems(self.locador)
        self.ui.pushButton_2.hide()
        self.cliente_2 = True

    def get_dados(self):
        lista_comprador_vendedor = []
        if self.cliente_2:
            self.cliente_2 = self.ui.comboBox_5.currentText()

        self.locador = self.ui.comboBox_2.currentText()
        self.corretor = self.ui.comboBox_3.currentText()
        
        return self.locador, self.corretor, self.cliente_2

    