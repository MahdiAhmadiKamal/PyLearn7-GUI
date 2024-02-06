import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.combo_


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.setWindowTitle("Unit Converter")
main_window.show()

main_window.comboBox.currentTextChanged.connect()

app.exec()