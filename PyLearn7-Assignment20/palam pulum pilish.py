import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *

score_player = 0
score_cpu1 = 0
score_cpu2 = 0

def play(player_choice):
    
    if player_choice == 1:
        main_window.player_board.setIcon(QIcon("pics/front-hand-player-96.png"))
    elif player_choice == 2:
        main_window.player_board.setIcon(QIcon("pics/back-hand-player-96.png"))

    cpu1_play()
    cpu2_play()
    check(player_choice, cpu1_choice, cpu2_choice)
    winer()

def cpu1_play():

    global cpu1_choice
    cpu1_choice = random.randint(1,2)
    if cpu1_choice == 1:
        main_window.cpu1_board.setIcon(QIcon("pics/front-hand-cpu1-96.png"))
    elif cpu1_choice == 2:
        main_window.cpu1_board.setIcon(QIcon("pics/back-hand-cpu1-96.png"))

def cpu2_play():

    global cpu2_choice
    cpu2_choice = random.randint(1,2)
    if cpu2_choice == 1:
        main_window.cpu2_board.setIcon(QIcon("pics/front-hand-cpu2-96.png"))
    elif cpu2_choice == 2:
        main_window.cpu2_board.setIcon(QIcon("pics/back-hand-cpu2-96.png"))

def check(player_choice, cpu1_choice, cpu2_choice):
    global score_player
    global score_cpu1
    global score_cpu2
    
    if player_choice != cpu1_choice and player_choice != cpu2_choice:
        score_player += 1
        main_window.score_player.setText(str(score_player))
        main_window.result_board.setIcon(QIcon("pics\icons8-arrow-96.png"))

    elif cpu1_choice != player_choice and cpu1_choice != cpu2_choice:
        score_cpu1 += 1
        main_window.score_cpu1.setText(str(score_cpu1))
        main_window.result_board.setIcon(QIcon("pics\icons8-arrow-96 (1).png"))

    elif cpu2_choice != player_choice and cpu2_choice != cpu1_choice:
        score_cpu2 += 1
        main_window.score_cpu2.setText(str(score_cpu2))
        main_window.result_board.setIcon(QIcon("pics\icons8-arrow-96 (2).png"))

def winer():
    if score_player == 5:
        ...
    elif score_cpu1 == 5:
        ...
    elif score_cpu2 == 5:
        ...


loader = QUiLoader()
app = QApplication(sys.argv)

main_window = loader.load("main_window.ui")
main_window.setWindowTitle("Palam Pulum Pilish")
main_window.show()

main_window.btn_front_hand.setIcon(QIcon("pics/front-hand-player-48.png"))
main_window.btn_back_hand.setIcon(QIcon("pics/back-hand-player-48.png"))

main_window.btn_front_hand.clicked.connect(partial(play, 1))
main_window.btn_back_hand.clicked.connect(partial(play, 2))

app.exec()