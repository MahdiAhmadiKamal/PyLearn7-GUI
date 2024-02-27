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
        self.line_edits = [[None for i in range(9)] for j in range(9)]
        self.new_game()
       
    def new_game(self):
        global cells
        cells = []
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)
        for i in range(9):
            for j in range(9):
                new_cell = QLineEdit()
                self.appearance(new_cell)
                
                if puzzle.board[i][j] != None:
                    new_cell.setText(str(puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.grid_layout.addWidget(new_cell, i, j)
                
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell
                cells.append(new_cell)

    def appearance(self, cell):
        cell.setAlignment(QtCore.Qt.AlignCenter)
        # cell.setFont(QFont("Segoe UI Black", 10))
        cell.setStyleSheet("background-color: #ffffff; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")
        
    def dark_light_mode(self):
        global flag
        if flag %2 == 0:
            self.ui.btn_dark_light_mode.setStyleSheet("background-color: #ffffff; font-size:11pt; color:'black'")
            self.ui.btn_dark_light_mode.setText("Light")
            self.setStyleSheet("background-color: #192a32")
            for cell in cells:
                cell.setStyleSheet("background-color: #25404d; height:50px;font-family:'Segoe UI Black'; font-size:20pt; color:'#f2b137'")
            flag += 1
        elif flag %2 != 0:
            self.ui.btn_dark_light_mode.setStyleSheet("background-color: #192a32; font-size:11pt; color:'#ffffff'")
            self.ui.btn_dark_light_mode.setText("Dark")
            self.setStyleSheet("background-color: #a8bec9")
            for cell in cells:
                cell.setStyleSheet("background-color: #ffffff; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")
            flag += 1

    def open_file(self):
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
                self.appearance(new_cell)
                if puzzle_board[i][j] != 0:
                    new_cell.setText(str(puzzle_board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.grid_layout.addWidget(new_cell, i, j)
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell

    def check(self):
        # for i in range(0,2):
        #     if i==0:
        #         for j in [1, 2, 3, 4, 5, 6, 7, 8]:
        #             number1 = self.line_edits[0][i].text()
        #             number2 = self.line_edits[0][j].text()
        #             if number1 == number2:
        #                 print("❌")
        #                 return False
        #     if i==1:   
        #         for j in [0, 2, 3, 4, 5, 6, 7, 8]:
        #             number3 = self.line_edits[0][i].text()
        #             number4 = self.line_edits[0][j].text()
        #             if number3 == number4:
        #                 print("❌❌")
        #                 return False
        array =[[None for i in range(9)] for j in range(9)]
        for i in range(0, 9):
            for j in range(0, 9):  
                array[i][j] = self.line_edits[i][j].text()
                if array[i][j] == '':
                    array[i][j] = None
                else:
                    array.append((array[i][j])) 
            new_row = [item for item in array[i] if item is not None]
            print(new_row)
            print(len(new_row))     
            print(len(set(new_row)))
            if len(new_row) != len(set(new_row)):
                print ("❌")
            # print(array[i])

        print('* * * * * * * * *')
        


    def validation(self, i, j, text):
        # text = self.line_edits[i][j].text()
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")

        self.check()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    app.exec()