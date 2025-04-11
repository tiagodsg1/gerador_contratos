from front.ui.pages.area.area import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow

from back.bd.update.logs.log_corretor import LogCorretor

class Area(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Área do Corretor")

        self.ui.pushButton_2.clicked.connect(self.insert_dados)

    def dados_corretor(self, corretor):
        self.ui.comboBox.addItems(corretor)

    def insert_dados(self):
        corretor = self.ui.comboBox.currentText()
        self.logs = LogCorretor().get_logs(corretor)
        print(self.logs)