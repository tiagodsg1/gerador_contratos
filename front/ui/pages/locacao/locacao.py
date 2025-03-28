# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'locacao.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(529, 595)
        Form.setStyleSheet("QLineEdit{\n"
"    border: 3px solid gray;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox{\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    border-left: 1px solid gray;\n"
"    width: 25px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image: url(:/icons/icons/down-arrow.png);\n"
"}\n"
"\n"
"QComboBox::down-arrow::hover{\n"
"    \n"
"    image: url(:/icons/icons/expand_circle_down_FILL0_wght400_GRAD0_opsz24.ico);\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 0px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"    border: 3px solid gray;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QDateEdit::down-arrow, QDateEdit::up-arrow {\n"
"    border: 0px;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QDateEdit::down-button, QDateEdit::up-button {\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border: none;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 507, 544))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setObjectName("widget")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(15, 60, 171, 21))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setGeometry(QtCore.QRect(255, 60, 171, 21))
        self.comboBox_5.setObjectName("comboBox_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(325, 50, 41, 41))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/1491254405-plusaddmoredetail_82972.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 160, 171, 21))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(170, 10, 121, 31))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setGeometry(QtCore.QRect(5, 100, 469, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(180, 120, 101, 31))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(150, 210, 16, 311))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(340, 210, 16, 311))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(15, 400, 131, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(10, 360, 151, 31))
        self.checkBox.setObjectName("checkBox")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(10, 270, 471, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(29, 200, 111, 31))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(200, 200, 101, 31))
        self.label_5.setObjectName("label_5")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 280, 151, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(15, 320, 131, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setGeometry(QtCore.QRect(170, 280, 181, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(180, 320, 131, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(360, 240, 121, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(400, 200, 51, 31))
        self.label_6.setObjectName("label_6")
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setGeometry(QtCore.QRect(170, 360, 151, 31))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_5.setGeometry(QtCore.QRect(360, 280, 121, 31))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 440, 161, 31))
        self.checkBox_6.setObjectName("checkBox_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setGeometry(QtCore.QRect(15, 480, 131, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.checkBox_7 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_7.setGeometry(QtCore.QRect(170, 400, 151, 31))
        self.checkBox_7.setObjectName("checkBox_7")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(360, 320, 131, 31))
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setScaledContents(False)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_8.setGeometry(QtCore.QRect(360, 360, 71, 31))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_9.setGeometry(QtCore.QRect(360, 400, 71, 31))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_10.setGeometry(QtCore.QRect(170, 440, 171, 31))
        self.checkBox_10.setAcceptDrops(False)
        self.checkBox_10.setAutoFillBackground(False)
        self.checkBox_10.setTristate(False)
        self.checkBox_10.setObjectName("checkBox_10")
        self.dateEdit = QtWidgets.QDateEdit(self.widget)
        self.dateEdit.setGeometry(QtCore.QRect(15, 240, 131, 22))
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_2.setGeometry(QtCore.QRect(180, 240, 131, 22))
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout.addWidget(self.widget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        
        self.comboBox_5.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_7.hide()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Variaveis"))
        self.label_3.setText(_translate("Form", "Parte locadora"))
        self.label_4.setText(_translate("Form", "Corretor"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "R$ "))
        self.checkBox.setText(_translate("Form", "Mudança no aluguel ?"))
        self.label_2.setText(_translate("Form", "Prazo do Contrato"))
        self.label_5.setText(_translate("Form", "Inicio do Contrato"))
        self.checkBox_2.setText(_translate("Form", "Mudança no IPTU ?"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "R$ "))
        self.checkBox_3.setText(_translate("Form", "Mudança no Condominio ?"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "R$ "))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "R$ "))
        self.label_6.setText(_translate("Form", "Seguro"))
        self.checkBox_4.setText(_translate("Form", "Fica em Condominio ?"))
        self.checkBox_5.setText(_translate("Form", "Aceita animais ?"))
        self.checkBox_6.setText(_translate("Form", "Maximo moradores"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "1 ou Mais"))
        self.checkBox_7.setText(_translate("Form", "Alienado ?"))
        self.label_7.setText(_translate("Form", "Relatorio de Entrega de chaves"))
        self.checkBox_8.setText(_translate("Form", "Agora ?"))
        self.checkBox_9.setText(_translate("Form", "Pós ?"))
        self.checkBox_10.setText(_translate("Form", "Inquilino pagará os \n"
"encargos de alocação ?"))
from front.static import resource
