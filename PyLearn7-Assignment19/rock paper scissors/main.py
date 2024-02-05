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
        main_window.player_board.setIcon(QIcon("pics/rock_100.png"))
    elif a == "paper":
        main_window.player_board.setIcon(QIcon("pics/paper_100.png"))
    elif a == "scissors":
        main_window.player_board.setIcon(QIcon("pics/scissors_100.png"))

    cpu_play()

def cpu_play():
    n = random.randint(1,3)
    if n == 1:
        main_window.cpu_board.setIcon(QIcon("pics/rock_101.png"))
    elif n == 2:
        main_window.cpu_board.setIcon(QIcon("pics/paper_101.png"))
    elif n == 3:
        main_window.cpu_board.setIcon(QIcon("pics/scissors_101.png"))



loader = QUiLoader()
app = QApplication(sys.argv)

main_window = loader.load("main_window.ui")
main_window.setWindowTitle("rock paper scissors")
main_window.show()

# main_window.score_player.setText(str(score_player))
# main_window.score_cpu.setText(str(score_cpu))

main_window.btn_rock.setIcon(QIcon("pics/rock_100.png"))
main_window.btn_paper.setIcon(QIcon("pics/paper_100.png"))
main_window.btn_scissors.setIcon(QIcon("pics/scissors_100.png"))
main_window.btn_rock.clicked.connect(partial(play, "rock"))
main_window.btn_paper.clicked.connect(partial(play, "paper"))
main_window.btn_scissors.clicked.connect(partial(play, "scissors"))

app.exec()