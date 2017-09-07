import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox,QFileDialog,QPlainTextEdit,QScrollArea
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
#from PyQt5.QtCore import pyqtSlot, QRect

class App(QMainWindow):

    def __init__(self, initial='', parent=None):
        super().__init__(parent)

        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setMaximumSize(400, 230)
        self.setMinimumSize(400, 230)
        self.resize(400, 230)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(5, 5, 390, 190))
        self.scrollArea.setWidgetResizable(True)

        self.plainTextEdit = QPlainTextEdit()
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 390, 190))
        self.plainTextEdit.setPlainText(initial)

        self.scrollArea.setWidget(self.plainTextEdit)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())