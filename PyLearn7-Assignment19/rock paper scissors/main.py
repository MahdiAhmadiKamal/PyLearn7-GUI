import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import *

score_player = 0
score_cpu = 0

def play(a):
    if a == "rock":
        main_window.player_board.setIcon(QIcon("images.png"))
    elif a == "paper":
        ...
    elif a == "scissors":
        ...

    cpu_play()

def cpu_play():
    ...



loader = QUiLoader()
app = QApplication(sys.argv)

main_window = loader.load("main_window.ui")
main_window.setWindowTitle("rock paper scissors")
main_window.show()

main_window.score_player.setText(str(score_player))
main_window.score_cpu.setText(str(score_cpu))

main_window.btn_rock.clicked.connect(partial(play, "rock"))
main_window.btn_paper.clicked.connect(partial(play, "paper"))
main_window.btn_scissors.clicked.connect(partial(play, "scissors"))

app.exec()