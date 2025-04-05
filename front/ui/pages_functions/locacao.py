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

    def insert_dados(self, cliente, corretor):
        self.locador = cliente
        self.locataria = cliente
        self.corretor = corretor
        self.hide_all()
        self.ui.comboBox_2.addItems(self.locador)
        self.ui.comboBox_3.addItems(self.corretor)
        self.ui.comboBox_4.addItems(self.locador)

    def hide_all(self):

        for line_edit in self.checkbox_lineedit_map.values():
            line_edit.hide()

    def get_dados(self):

        self.locador = self.ui.comboBox_4.currentText()
        self.locataria = self.ui.comboBox_2.currentText()
        self.corretor = self.ui.comboBox_3.currentText()


        inicio_contr = self.ui.dateEdit.date()
        praz_contr = self.ui.dateEdit_2.date()
        seguro = self.ui.lineEdit_6.text()

        cartorio = self.ui.lineEdit_8.text()
        n_iptu = self.ui.lineEdit_9.text()
        relogio = self.ui.lineEdit_10.text()
        monobitrifasico = self.ui.lineEdit_13.text()
        agua = self.ui.lineEdit_16.text()
        gas = self.ui.lineEdit_14.text()
        funesbom = self.ui.lineEdit_15.text()
        matricula = self.ui.lineEdit_11.text()
        luz = self.ui.lineEdit_12.text()

        fim_contr = inicio_contr.month() + praz_contr.month()
        if fim_contr > 12:
            dia = inicio_contr.day()
            mes = fim_contr - 12
            ano = inicio_contr.year() + 1
        else:
            dia = inicio_contr.day()
            mes = fim_contr
            ano = inicio_contr.year()
        if mes < 10:
            mes = f'0{mes}'
        if dia < 10:
            dia = f'0{dia}'
        fim_contr = f"{dia}/{mes}/{ano}"
        inicio_contr = f'{inicio_contr.day()}/{inicio_contr.month()}/{inicio_contr.year()}'
        praz_contr = f'{praz_contr.month()}'

        self.info_ad = {
                    'inicio_contr': inicio_contr,
                    'praz_contr': praz_contr,
                    'fim_contr': fim_contr,
                    'seguro': seguro,
                    'fim_contr': None,
                    'iptu': None,
                    'cond': None,
                    'aluguel': None,
                    'max_moradores': None,
                    'cartorio' : cartorio,
                    'n_iptu': n_iptu,
                    'relogio': relogio,
                    'monobitrifasico': monobitrifasico,
                    'agua': agua,
                    'luz': luz,
                    'gas': gas,
                    'funesbom': funesbom,
                    'matricula': matricula,
                    'act_anm': False,
                    'fic_cond': False,
                    'alienado': False,
                    'enc_loc': False,
                    'chav_agr': False,
                    'chav_post': False,
                    'garagem': False,
                    'vist_agr': False,
                    'vist_post': False,
        }

        self.info_ad["fim_contr"] = fim_contr
        if self.ui.checkBox_2.isChecked():
            valor = self.ui.lineEdit_4.text()
            self.info_ad["iptu"] = valor
        
        if self.ui.checkBox_3.isChecked():
            valor = self.ui.lineEdit_5.text()
            self.info_ad["cond"] = valor

        if self.ui.checkBox.isChecked():
            valor = self.ui.lineEdit_3.text()
            self.info_ad["aluguel"] = valor

        if self.ui.checkBox_6.isChecked():
            valor = self.ui.lineEdit_7.text()
            self.info_ad["max_moradores"] = valor

        if self.ui.checkBox_5.isChecked() : self.info_ad["act_anm"] = True
        if self.ui.checkBox_4.isChecked() : self.info_ad["fic_cond"] = True
        if self.ui.checkBox_7.isChecked() : self.info_ad["alienado"] = True
        if self.ui.checkBox_10.isChecked() : self.info_ad["enc_loc"] = True
        if self.ui.checkBox_8.isChecked() : self.info_ad["chav_agr"] = True
        if self.ui.checkBox_9.isChecked() : self.info_ad["chav_post"] = True
        if self.ui.checkBox_11.isChecked() : self.info_ad["garagem"] = True
        if self.ui.checkBox_12.isChecked() : self.info_ad["vist_agr"] = True
        if self.ui.checkBox_13.isChecked() : self.info_ad["vist_post"] = True
        
        return self.locador, self.locataria, self.corretor, self.info_ad

    