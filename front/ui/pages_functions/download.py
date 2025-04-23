from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox

from front.ui.pages.download.download import Download_Form

class Download(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Download_Form()
        self.ui.setupUi(self)
        self.show()

    def change_label(self, text):
        self.ui.label.setText(text)

    def change_progress(self, value):
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setValue(value)
