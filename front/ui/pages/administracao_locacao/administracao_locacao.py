# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administracao_locacao.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 594)
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
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 350, 121, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(420, 90, 41, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/1491254405-plusaddmoredetail_82972.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 70, 211, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 240, 41, 41))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.layoutWidget_2 = QtWidgets.QWidget(Form)
        self.layoutWidget_2.setGeometry(QtCore.QRect(90, 220, 211, 71))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_3.addWidget(self.comboBox_3)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 70, 211, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(250, 500, 121, 22))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_16 = QtWidgets.QLineEdit(Form)
        self.lineEdit_16.setGeometry(QtCore.QRect(390, 350, 121, 22))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(250, 400, 121, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(250, 450, 121, 22))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(390, 500, 121, 22))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(250, 350, 121, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(390, 400, 121, 22))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(390, 450, 121, 22))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(320, 550, 121, 22))
        self.lineEdit_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.layoutWidget.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton.raise_()
        self.lineEdit_13.raise_()
        self.lineEdit_16.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_14.raise_()
        self.lineEdit_15.raise_()
        self.lineEdit_12.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Variaveis"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Porcertagem"))
        self.label_3.setText(_translate("Form", "Escolha o Locador"))
        self.label_4.setText(_translate("Form", "Escolha o Locador"))
        self.label_2.setText(_translate("Form", "Escolha o Locador"))
        self.lineEdit_13.setPlaceholderText(_translate("Form", "Monobitrifasico"))
        self.lineEdit_16.setPlaceholderText(_translate("Form", "Nº Cons D\'Água"))
        self.lineEdit_9.setPlaceholderText(_translate("Form", "Inscrição IPTU"))
        self.lineEdit_10.setPlaceholderText(_translate("Form", "Relogio"))
        self.lineEdit_11.setPlaceholderText(_translate("Form", "Matricula"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "Cartorio"))
        self.lineEdit_14.setPlaceholderText(_translate("Form", "Nº Cons Gás"))
        self.lineEdit_15.setPlaceholderText(_translate("Form", "Funesbom"))
        self.lineEdit_12.setPlaceholderText(_translate("Form", "Nº Cons Luz"))
from front.static import resource
