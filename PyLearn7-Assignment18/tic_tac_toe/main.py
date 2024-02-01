import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

count = []
score_x = 0
score_o = 0
score_tie = 0

def about():
    f = open("about.txt", "r")
    r = f.read()
    about_box = QMessageBox(text=r)
    about_box.setWindowTitle("about Tic Tac Toe")
    about_box.exec()
    
def add_score():
    global player
    global score_x
    global score_o

    if player == "Player 1" or player == "Player":
        score_x += 1
        main_window.scoreboard_x.setText(str(score_x))
    elif player == "Player 2" or player == "cpu":
        score_o += 1
        main_window.scoreboard_o.setText(str(score_o))

def check(row, col):
    global player
    global score_tie

    if buttons[row][0].text()==buttons[row][1].text()==buttons[row][2].text()!="" or \
    buttons[0][col].text()==buttons[1][col].text()==buttons[2][col].text()!="":
        
        add_score()
        msg_box = QMessageBox(text= player+ " wins!")
        msg_box.exec()
        new_game()
    elif buttons[0][0].text()==buttons[1][1].text()==buttons[2][2].text()!="" or \
    buttons[0][2].text()==buttons[1][1].text()==buttons[2][0].text()!="":
        
        add_score()
        msg_box = QMessageBox(text= player+ " wins!")
        msg_box.exec()
        new_game()
    elif len(count) == 9:
        score_tie += 1
        main_window.scoreboard_tie.setText(str(score_tie))
        msg_box = QMessageBox(text="Tie")
        msg_box.exec()
        new_game()


def play(row, col):
    
    global player
    
    if player == "Player 1":
        if buttons[row][col].text()=="":
            buttons[row][col].setText("X")
            buttons[row][col].setStyleSheet("color: #31c3bc; border-radius:15px;")
            count.append("1")
            check(row, col)
            player = "Player 2"
    elif player == "Player 2":
        if buttons[row][col].text()=="":
            buttons[row][col].setText("O")
            buttons[row][col].setStyleSheet("color: #f2b137; border-radius:15px;")
            count.append("2")
            check(row, col)
            player = "Player 1"
    elif player == "Player":
        if buttons[row][col].text()=="":
            buttons[row][col].setText("X")
            buttons[row][col].setStyleSheet("color: #31c3bc; border-radius:15px;")
            count.append("1")
            check(row, col)
            player = "cpu"
            game_mode_1()
        



def new_game():
    count.clear()
    for row in range(3):
        for col in range (3):
            buttons[row][col].setText("")
            buttons[row][col].setStyleSheet("")


def game_mode_1():
    global player
    if player == "cpu":
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            
            if buttons[row][col].text()=="":
                buttons[row][col].setText("O")
                buttons[row][col].setStyleSheet("color: #f2b137; border-radius:15px;")
                count.append("2")
                break
        check(row, col)
        player = "Player"
    elif player == "Player":
        for i in range (3):
            for j in range (3):
                buttons[i][j].clicked.connect(partial(play, i, j))
    

def game_mode_2():
    global player
    player = "Player 1"
    for i in range (3):
        for j in range (3):
            buttons[i][j].clicked.connect(partial(play, i, j))

loader = QUiLoader()
app = QApplication(sys.argv)



player = "Player"

main_window = loader.load("main_window.ui")
main_window.setWindowTitle("Tic Tac Toe")
main_window.show()

main_window.scoreboard_x.setText(str(score_x))
main_window.scoreboard_o.setText(str(score_o))
main_window.scoreboard_tie.setText(str(score_tie))

buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
           [main_window.btn_4, main_window.btn_5, main_window.btn_6],
           [main_window.btn_7, main_window.btn_8, main_window.btn_9]]

# for i in range (3):
#     for j in range (3):
#         buttons[i][j].clicked.connect(partial(play, i, j))


main_window.btn_new_game.clicked.connect(new_game)
main_window.player_vs_cpu.clicked.connect(game_mode_1)
main_window.player_vs_player.clicked.connect(game_mode_2)
main_window.btn_about.clicked.connect(about)



app.exec()