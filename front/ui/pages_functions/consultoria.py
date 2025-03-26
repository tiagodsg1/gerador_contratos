from front.ui.pages.consultoria.consultoria import Ui_Form
from PyQt5.QtWidgets import QWidget

class consultoria(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.checkbox_lineedit_map = {
            self.ui.checkBox_2: self.ui.lineEdit_4,
            self.ui.checkBox_4: self.ui.lineEdit_6,
        }
        for checkbox, line_edit in self.checkbox_lineedit_map.items():
            checkbox.stateChanged.connect(
                lambda state, le=line_edit: le.setVisible(state == 2)
            )

    def insert_dados(self, corretor):
        self.corretor = corretor
        self.hide_all()
        self.ui.comboBox_3.addItems(self.corretor)

    def hide_all(self):
        for line_edit in self.checkbox_lineedit_map.values():
            line_edit.hide()

    def get_dados(self):
        min_valor = None
        av_valor = None
        if self.ui.checkBox_2.isChecked():
            min_valor = self.ui.lineEdit_4.text()
        
        if self.ui.checkBox_4.isChecked():
            av_valor = self.ui.lineEdit_6.text()
        
        pro_valor = self.ui.lineEdit_7.text()
        cons_valor = self.ui.lineEdit_8.text()
        self.corretor = self.ui.comboBox_3.currentText()
        return self.corretor, min_valor, av_valor, pro_valor, cons_valor

    

