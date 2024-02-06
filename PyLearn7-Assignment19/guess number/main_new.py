import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *

def play():
    # gussed_num = int(main_window.txtbox.text())
    check()

def check():
    guessed_num = int(main_window.txtbox.text())
    num = random.randint(10,100)
    if guessed_num > num:
        print("come down")
        print(num)
    elif guessed_num < num:
        print("go up")
        print(num)
    elif guessed_num == num:
        print("bingo")


loader = QUiLoader()
app = QApplication(sys.argv)

main_window = loader.load("mainwindow.ui")
main_window.setWindowTitle("Guess Number")
main_window.show()

main_window.btn_check.clicked.connect(check)

app.exec()