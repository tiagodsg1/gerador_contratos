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
        Form.resize(625, 597)
        Form.setStyleSheet("QLineEdit{\n"
"    border: 3px solid gray;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QComboBox{\n"
"    border: 2px solid gray;\n"
"    border-radius: 10px;\n"
"    padding-left: 6px;\n"
"    padding-bottom: 2px;\n"
"    padding-top: 2px;\n"
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(11, 11, 82, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(11, 40, 601, 541))
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -525, 580, 1071))
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(510, 1071))
        self.scrollAreaWidgetContents.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(0, 20, 581, 1071))
        self.widget.setMinimumSize(QtCore.QSize(488, 523))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setObjectName("widget")
        self.line_6 = QtWidgets.QFrame(self.widget)
        self.line_6.setGeometry(QtCore.QRect(-2, 290, 481, 20))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(205, 460, 21, 611))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(5, 650, 131, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(0, 600, 171, 41))
        self.checkBox.setObjectName("checkBox")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(0, 520, 571, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_2.setGeometry(QtCore.QRect(0, 530, 231, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(5, 570, 131, 22))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_3.setGeometry(QtCore.QRect(225, 530, 151, 31))
        self.checkBox_3.setTristate(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(235, 570, 131, 22))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_4.setGeometry(QtCore.QRect(225, 610, 171, 31))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_5.setGeometry(QtCore.QRect(390, 540, 121, 31))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_6.setGeometry(QtCore.QRect(0, 690, 201, 31))
        self.checkBox_6.setObjectName("checkBox_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setGeometry(QtCore.QRect(5, 730, 131, 22))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.checkBox_7 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_7.setGeometry(QtCore.QRect(225, 650, 161, 31))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_10 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_10.setGeometry(QtCore.QRect(0, 450, 211, 61))
        self.checkBox_10.setAcceptDrops(False)
        self.checkBox_10.setAutoFillBackground(False)
        self.checkBox_10.setTristate(False)
        self.checkBox_10.setObjectName("checkBox_10")
        self.line_7 = QtWidgets.QFrame(self.widget)
        self.line_7.setGeometry(QtCore.QRect(0, 140, 481, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.checkBox_11 = QtWidgets.QCheckBox(self.widget)
        self.checkBox_11.setGeometry(QtCore.QRect(225, 710, 161, 31))
        self.checkBox_11.setObjectName("checkBox_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setGeometry(QtCore.QRect(260, 790, 121, 22))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setGeometry(QtCore.QRect(260, 840, 121, 22))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setGeometry(QtCore.QRect(260, 890, 121, 22))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_11.setGeometry(QtCore.QRect(400, 790, 121, 22))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_12.setGeometry(QtCore.QRect(330, 990, 121, 22))
        self.lineEdit_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_13.setGeometry(QtCore.QRect(260, 940, 121, 22))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_14.setGeometry(QtCore.QRect(400, 840, 121, 22))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_15.setGeometry(QtCore.QRect(400, 890, 121, 22))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_16.setGeometry(QtCore.QRect(400, 940, 121, 22))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.line_5 = QtWidgets.QFrame(self.widget)
        self.line_5.setGeometry(QtCore.QRect(0, 680, 571, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_9 = QtWidgets.QFrame(self.widget)
        self.line_9.setGeometry(QtCore.QRect(0, 760, 561, 20))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.layoutWidget = QtWidgets.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 320, 341, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(339, 0))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_18.setGeometry(QtCore.QRect(390, 740, 161, 22))
        self.lineEdit_18.setMinimumSize(QtCore.QSize(161, 22))
        self.lineEdit_18.setMaximumSize(QtCore.QSize(161, 22))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.line_10 = QtWidgets.QFrame(self.widget)
        self.line_10.setGeometry(QtCore.QRect(370, 690, 20, 81))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(370, 460, 21, 231))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.layoutWidget1 = QtWidgets.QWidget(self.widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 920, 191, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_8 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_8.setObjectName("checkBox_8")
        self.horizontalLayout.addWidget(self.checkBox_8)
        self.checkBox_9 = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_9.setObjectName("checkBox_9")
        self.horizontalLayout.addWidget(self.checkBox_9)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.layoutWidget2 = QtWidgets.QWidget(self.widget)
        self.layoutWidget2.setGeometry(QtCore.QRect(390, 610, 114, 51))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setReadOnly(False)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.verticalLayout_5.addWidget(self.lineEdit_17)
        self.layoutWidget3 = QtWidgets.QWidget(self.widget)
        self.layoutWidget3.setGeometry(QtCore.QRect(0, 790, 161, 81))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget3)
        self.label_9.setTextFormat(QtCore.Qt.AutoText)
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_6.addWidget(self.label_9)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_12 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_12.setObjectName("checkBox_12")
        self.horizontalLayout_2.addWidget(self.checkBox_12)
        self.checkBox_13 = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_13.setObjectName("checkBox_13")
        self.horizontalLayout_2.addWidget(self.checkBox_13)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.layoutWidget4 = QtWidgets.QWidget(self.widget)
        self.layoutWidget4.setGeometry(QtCore.QRect(390, 460, 141, 55))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget4)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(121, 22))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(121, 22))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_4.addWidget(self.lineEdit_6)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_4)
        self.layoutWidget5 = QtWidgets.QWidget(self.widget)
        self.layoutWidget5.setGeometry(QtCore.QRect(220, 460, 151, 54))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.layoutWidget5)
        self.dateEdit_2.setMinimumSize(QtCore.QSize(131, 21))
        self.dateEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_5.addWidget(self.dateEdit_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(420, 700, 111, 31))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.layoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 532, 101))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.radioButton.setMinimumSize(QtCore.QSize(80, 0))
        self.radioButton.setText("")
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_7.addWidget(self.radioButton)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.verticalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem11)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_8.addWidget(self.comboBox)
        spacerItem12 = QtWidgets.QSpacerItem(13, 36, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem12)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_4.setEnabled(False)
        self.comboBox_4.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_8.addWidget(self.comboBox_4)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem13)
        self.verticalLayout_9.addLayout(self.horizontalLayout_8)
        self.layoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 170, 532, 101))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_10.addWidget(self.label_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem15)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.radioButton_2.setMinimumSize(QtCore.QSize(80, 0))
        self.radioButton_2.setText("")
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_9.addWidget(self.radioButton_2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem16)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem17)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget_3)
        self.comboBox_2.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_10.addWidget(self.comboBox_2)
        spacerItem18 = QtWidgets.QSpacerItem(13, 36, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem18)
        self.comboBox_5 = QtWidgets.QComboBox(self.layoutWidget_3)
        self.comboBox_5.setEnabled(False)
        self.comboBox_5.setMinimumSize(QtCore.QSize(250, 0))
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_10.addWidget(self.comboBox_5)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem19)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.line_10.raise_()
        self.line_2.raise_()
        self.line_6.raise_()
        self.line.raise_()
        self.lineEdit_3.raise_()
        self.checkBox.raise_()
        self.line_3.raise_()
        self.checkBox_2.raise_()
        self.lineEdit_4.raise_()
        self.checkBox_3.raise_()
        self.lineEdit_5.raise_()
        self.checkBox_4.raise_()
        self.checkBox_5.raise_()
        self.checkBox_6.raise_()
        self.lineEdit_7.raise_()
        self.checkBox_7.raise_()
        self.checkBox_10.raise_()
        self.line_7.raise_()
        self.checkBox_11.raise_()
        self.lineEdit_8.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.lineEdit_11.raise_()
        self.lineEdit_12.raise_()
        self.lineEdit_13.raise_()
        self.lineEdit_14.raise_()
        self.lineEdit_15.raise_()
        self.lineEdit_16.raise_()
        self.line_5.raise_()
        self.line_9.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget.raise_()
        self.lineEdit_18.raise_()
        self.label_10.raise_()
        self.layoutWidget_2.raise_()
        self.layoutWidget_3.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.lineEdit_5.hide()
        self.lineEdit_7.hide()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Variaveis"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "R$ "))
        self.checkBox.setText(_translate("Form", "Houve Mudança no valor\n"
"aluguel ?"))
        self.checkBox_2.setText(_translate("Form", "Houve mudança no valor IPTU ?"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "R$ "))
        self.checkBox_3.setText(_translate("Form", "Houve Mudança no\n"
"valor Condominio ?"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "R$ "))
        self.checkBox_4.setText(_translate("Form", "Fica em Condominio ?"))
        self.checkBox_5.setText(_translate("Form", "Aceita animais ?"))
        self.checkBox_6.setText(_translate("Form", "Limite maximo de moradores"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", "1 ou Mais"))
        self.checkBox_7.setText(_translate("Form", "O imovel é alienado ?"))
        self.checkBox_10.setText(_translate("Form", "Marque caso a Parte Locatária\n"
"seja aresponsável por pagar os\n"
"encargos da locação"))
        self.checkBox_11.setText(_translate("Form", "Garagem disponivel ?"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", "Cartorio"))
        self.lineEdit_9.setPlaceholderText(_translate("Form", "Inscrição IPTU"))
        self.lineEdit_10.setPlaceholderText(_translate("Form", "Relogio"))
        self.lineEdit_11.setPlaceholderText(_translate("Form", "Matricula"))
        self.lineEdit_12.setPlaceholderText(_translate("Form", "Nº Cons Luz"))
        self.lineEdit_13.setPlaceholderText(_translate("Form", "Monobitrifasico"))
        self.lineEdit_14.setPlaceholderText(_translate("Form", "Nº Cons Gás"))
        self.lineEdit_15.setPlaceholderText(_translate("Form", "Funesbom"))
        self.lineEdit_16.setPlaceholderText(_translate("Form", "Nº Cons D\'Água"))
        self.label_4.setText(_translate("Form", "Corretor"))
        self.lineEdit_18.setPlaceholderText(_translate("Form", "Dia de vencimento"))
        self.label_7.setText(_translate("Form", "O recibo de entrega de chaves será entregue agora ou depois?"))
        self.checkBox_8.setText(_translate("Form", "Agora"))
        self.checkBox_9.setText(_translate("Form", "Pós "))
        self.label_2.setText(_translate("Form", "Prazo do Contrato"))
        self.lineEdit_17.setPlaceholderText(_translate("Form", "30 meses"))
        self.label_9.setText(_translate("Form", "O relatório de vistoria será enviado agora ou após a entrega das chaves?"))
        self.checkBox_12.setText(_translate("Form", "Agora"))
        self.checkBox_13.setText(_translate("Form", "Pós"))
        self.label_6.setText(_translate("Form", "Seguro Residencial"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "R$ "))
        self.label_5.setText(_translate("Form", "Inicio do Contrato"))
        self.label_10.setText(_translate("Form", "Dia de vencimento do contrato"))
        self.label_8.setText(_translate("Form", "Parte Locataria"))
        self.label_11.setText(_translate("Form", "Parte Locadora"))
from front.static import resource
