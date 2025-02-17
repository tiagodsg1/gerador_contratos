from PyQt5.QtWidgets import QFileDialog

def save_document(doc):
    file_name, _ = QFileDialog.getSaveFileName(None, "Save Document", "", "Word Document (*.docx)")
    if file_name:
        return file_name