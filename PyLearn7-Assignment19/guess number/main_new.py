import sys
import random
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import *


number = random.randint(10,100)
count = 0

def check():
    global count
    while True:
        guessed_number = int(main_window.txtbox.text())
        count = count +1

        if number == guessed_number:
            main_window.result_board.setText("Congratulations, you win!")
            main_window.result_board_2.setText("You succeeded after")
            main_window.result_board_2_1.setText(str(count))
            main_window.result_board_2_2.setText("tries.")
            main_window.result_board_3.setIcon(QIcon("pics/icons8-congratulations-100.png"))
            
            break

        elif number > guessed_number:
            main_window.result_board.setText("Go up. ⬆")
            break
        elif number < guessed_number:
            main_window.result_board.setText("Go down. ⬇")
            break


loader = QUiLoader()
app = QApplication(sys.argv)

main_window = loader.load("mainwindow.ui")
main_window.setWindowTitle("Guess Number")
main_window.show()

main_window.board.setText("Pick a number between 10 to 100.")
main_window.btn_check.clicked.connect(check)

app.exec()