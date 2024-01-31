import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

count = []


def check(row, col):
    global player

    if buttons[row][0].text()==buttons[row][1].text()==buttons[row][2].text()!="" or \
    buttons[0][col].text()==buttons[1][col].text()==buttons[2][col].text()!="":
        if player == "Player 1":
            player = "Player 2"
        elif player == "Player 2":
            player = "Player 1"
        msg_box = QMessageBox(text= player+ " wins!")
        msg_box.exec()
    elif buttons[0][0].text()==buttons[1][1].text()==buttons[2][2].text()!="" or \
    buttons[0][2].text()==buttons[1][1].text()==buttons[2][0].text()!="":
        if player == "Player 1":
            player = "Player 2"
        elif player == "Player 2":
            player = "Player 1"
        msg_box = QMessageBox(text= player+ " wins!")
        msg_box.exec()
    elif len(count) == 9:
        msg_box = QMessageBox(text="Draw")
        msg_box.exec()


def play(row, col):
    
    global player
    
    if player == "Player 1":
        buttons[row][col].setText("X")
        buttons[row][col].setStyleSheet("color: red; background-color: pink;")
        count.append("1")
        player = "Player 2"
    elif player == "Player 2":
        buttons[row][col].setText("O")
        buttons[row][col].setStyleSheet("color: blue; background-color: lightblue")
        count.append("2")
        player = "Player 1"

    check(row, col)

def newgame():
    for row in range(3):
        for col in range (3):
            buttons[row][col].setText("")
            buttons[row][col].setStyleSheet("")

    

loader = QUiLoader()
app = QApplication(sys.argv)

player = "Player 1"

main_window = loader.load("main_window.ui")
main_window.show()

buttons = [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
           [main_window.btn_4, main_window.btn_5, main_window.btn_6],
           [main_window.btn_7, main_window.btn_8, main_window.btn_9]]

for i in range (3):
    for j in range (3):
        buttons[i][j].clicked.connect(partial(play, i, j))

main_window.btn_newgame.clicked.connect(newgame)


app.exec()