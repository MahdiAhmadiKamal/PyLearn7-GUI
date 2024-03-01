import sys
import random
from functools import partial
from sudoku import Sudoku
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6 import QtWidgets, QtCore
from main_window import Ui_MainWindow


flag = 0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("background-color: #a8bec9")
        self.ui.btn_dark_light_mode.setStyleSheet("background-color: #192a32; font-size:11pt; color:'#ffffff'")
        self.ui.btn_dark_light_mode.clicked.connect(partial(self.dark_light_mode))
        self.ui.menu_new.triggered.connect(self.new_game)
        self.ui.menu_open_file.triggered.connect(self.open_file)
        self.ui.menu_puzzle_answer.triggered.connect(self.puzzle_answer)
        self.ui.menu_about.triggered.connect(self.about)
        self.ui.menu_exit.triggered.connect(self.exit)
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        self.new_game()
    
    def new_game(self):
        
        self.puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)
        self.show_game()
        solve = self.puzzle.solve()
        # print(solve.board)

    def show_game(self):
        global cells
        global new_cell
        global puzzle_board
        cells = []
        
        # puzzle_board = [[None for i in range(9)] for j in range(9)]
        
        for i in range(9):
            for j in range(9):
            
                new_cell = QLineEdit()
                self.appearance(new_cell, "correct_light")
                
                if self.puzzle.board[i][j] != None:
                    # puzzle_board[i][j]=self.puzzle.board[i][j]
                    new_cell.setText(str(self.puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.grid_layout.addWidget(new_cell, i, j)
                
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell
                cells.append(new_cell)
           
            # puzzle_board[i] = self.puzzle.board[i]
            # print(puzzle_board[i])

    def appearance(self, cell, status):
        cell.setAlignment(QtCore.Qt.AlignCenter)
        if status == "correct_light":
            cell.setStyleSheet("background-color: #ffffff; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")
        elif status == "incorrect_light":
            cell.setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")
        elif status == "correct_dark":
            cell.setStyleSheet("background-color: #25404d; height:50px;font-family:'Segoe UI Black'; font-size:20pt; color:'#f2b137'")
        
    def dark_light_mode(self):
        global flag
        if flag %2 == 0:
            self.ui.btn_dark_light_mode.setStyleSheet("background-color: #ffffff; font-size:11pt; color:'black'")
            self.ui.btn_dark_light_mode.setText("Light")
            self.setStyleSheet("background-color: #192a32")
            for cell in cells:
                self.appearance(cell, "correct_dark")
            flag += 1
        elif flag %2 != 0:
            self.ui.btn_dark_light_mode.setStyleSheet("background-color: #192a32; font-size:11pt; color:'#ffffff'")
            self.ui.btn_dark_light_mode.setText("Dark")
            self.setStyleSheet("background-color: #a8bec9")
            for cell in cells:
                self.appearance(cell, "correct_light")
            flag += 1

    def open_file(self):
        try:
            file_path = QFileDialog.getOpenFileName(self, "Open file...")[0]
            f = open(file_path, "r")
            big_text = f.read()
            rows = big_text.split("\n")
            puzzle_board = [[None for i in range(9)] for j in range(9)]
            for i in range(len(rows)):
                cells = rows[i].split(" ")
                for j in range(len(cells)):
                    puzzle_board[i][j] = int(cells[j])

            for i in range(9):
                for j in range(9):
                    new_cell = QLineEdit()
                    self.appearance(new_cell, "correct_light")
                    if puzzle_board[i][j] != 0:
                        new_cell.setText(str(puzzle_board[i][j]))
                        new_cell.setReadOnly(True)
                    self.ui.grid_layout.addWidget(new_cell, i, j)
                    new_cell.textChanged.connect(partial(self.validation, i, j))
                    self.line_edits[i][j] = new_cell
        except:
            msg = QMessageBox()
            msg.setText('An error occurred!')
            msg.exec()

    def check(self, i, j, text):
        #row check
        for i1 in range(0, 9):
            for j1 in range(0, 9):
                num = self.line_edits[i1][j1].text()
                if num == text and i == i1 and j != j1:
                    self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")
        
        #column check
        for i2 in range(0, 9):
            for j2 in range(0, 9):
                num = self.line_edits[i2][j2].text()
                if num == text and i != i2 and j == j2:
                    self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")   

        #3x3 square check 
        #(top-left)
        if 0 <= i < 3 and 0 <= j < 3 :
            for i3 in range(0, 3):
                for j3 in range(0, 3):
                    num = self.line_edits[i3][j3].text()
                    if num == text and i != i3 and j != j3:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")   

        #(top-center)
        if 0 <= i < 3 and 3 <= j < 6 :
            for i4 in range(0, 3):
                for j4 in range(3, 6):
                    num = self.line_edits[i4][j4].text()
                    if num == text and i != i4 and j != j4:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")   

        #(top-right)
        if 0 <= i < 3 and 6 <= j < 9 :
            for i5 in range(0, 3):
                for j5 in range(6, 9):
                    num = self.line_edits[i5][j5].text()
                    if num == text and i != i5 and j != j5:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")   

        #(middle-left)
        if 3 <= i < 6 and 0 <= j < 3 :
            for i6 in range(3, 6):
                for j6 in range(0, 3):
                    num = self.line_edits[i6][j6].text()
                    if num == text and i != i6 and j != j6:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")   

        #(middle-center)
        if 3 <= i < 6 and 3 <= j < 6 :
            for i7 in range(3, 6):
                for j7 in range(3, 6):
                    num = self.line_edits[i7][j7].text()
                    if num == text and i != i7 and j != j7:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")   

        #(middle-right)
        if 3 <= i < 6 and 6 <= j < 9 :
            for i8 in range(3, 6):
                for j8 in range(6, 9):
                    num = self.line_edits[i8][j8].text()
                    if num == text and i != i8 and j != j8:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")        

        #(bottom-left)
        if 6 <= i < 9 and 0 <= j < 3 :
            for i9 in range(6, 9):
                for j9 in range(0, 3):
                    num = self.line_edits[i9][j9].text()
                    if num == text and i != i9 and j != j9:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")   

        #(bottom-center)
        if 6 <= i < 9 and 3 <= j < 6 :
            for i10 in range(6, 9):
                for j10 in range(3, 6):
                    num = self.line_edits[i10][j10].text()
                    if num == text and i != i10 and j != j10:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")   

        #(bottom-right)
        if 6 <= i < 9 and 6 <= j < 9 :
            for i11 in range(6, 9):
                for j11 in range(6, 9):
                    num = self.line_edits[i11][j11].text()
                    if num == text and i != i11 and j != j11:
                        self.line_edits[i][j].setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")                         

    def win_check(self):
        # print("check")
        play_board = [[None for i in range(9)] for j in range(9)]
        answer_board = [[None for i in range(9)] for j in range(9)]
        solve = self.puzzle.solve()
        for ii in range(9):
            for jj in range(9):
                play_board[ii][jj] = self.line_edits[ii][jj].text()
                answer_board[ii][jj] = str(solve.board[ii][jj])

        if play_board == answer_board:
            print("*** You Win! ***")
            msg = QMessageBox()
            msg.setText('*** You Win! ***')
            msg.exec()
                  

    def puzzle_answer(self):
        solve = self.puzzle.solve()
        print(solve.board)
        self.puzzle = Sudoku(3, 3, board=solve.board)
        self.show_game()

    def validation(self, i, j, text):
        # text = self.line_edits[i][j].text()
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")

        self.check(i, j, text)
        # puzzle_board[i][j]= text
        # print(puzzle_board)
        self.win_check()

    def about(self):
        f = open("about.txt", "r")
        r = f.read()
        about_box = QMessageBox(text=r)
        about_box.setWindowTitle("about Sudoku")
        about_box.exec()

    def exit(self):
        exit(0)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    app.exec()