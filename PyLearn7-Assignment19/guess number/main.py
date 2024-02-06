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

        self.text_box = self.ui.txtbox
        self.ckeck_button = self.ui.btn_check

    def play(self):
        number = self.text_box.text()

    def check(self):
        if self.text_box.text() == 0:
            print("yes")


app = QApplication(sys.argv)

main_window = MainWindow()
main_window.setWindowTitle("Guess Number")
main_window.show()


app.exec()