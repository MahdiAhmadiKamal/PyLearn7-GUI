import sys
import random
import collections
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
        global new_cell
        global puzzle_board
        cells = []
        puzzle = Sudoku(3, seed=random.randint(1, 1000)).difficulty(0.5)
        puzzle_board = [[None for i in range(9)] for j in range(9)]
        
        for i in range(9):
            for j in range(9):
            
                new_cell = QLineEdit()
                self.appearance(new_cell, "correct")
                
                if puzzle.board[i][j] != None:
                    puzzle_board[i][j]=puzzle.board[i][j]
                    new_cell.setText(str(puzzle.board[i][j]))
                    new_cell.setReadOnly(True)
                self.ui.grid_layout.addWidget(new_cell, i, j)
                
                new_cell.textChanged.connect(partial(self.validation, i, j))
                self.line_edits[i][j] = new_cell
                cells.append(new_cell)
            # puzzle_board = puzzle.board[i]
            # print(puzzle_board[i])
        # print('* * * * * * * * *')

    def appearance(self, cell, status):
        cell.setAlignment(QtCore.Qt.AlignCenter)
        # cell.setFont(QFont("Segoe UI Black", 10))
        if status == "correct":
            cell.setStyleSheet("background-color: #ffffff; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")
        elif status == "incorrect":
            cell.setStyleSheet("background-color: #ff909b; height:50px;font-family:'Segoe UI Black'; font-size:20pt;")
    
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

    def check(self, i, j):
        global array
        global array_tr
        array =[[None for i in range(9)] for j in range(9)]
        # array_tr = []
        array_tr = [[None for i in range(9)] for j in range(9)]
        puzzle_board_tr = [[None for i in range(9)] for j in range(9)]
        
        for i in range(0, 9):
            for j in range(0, 9):  
                array[i][j] = self.line_edits[i][j].text()
                
                if array[i][j] == '':
                    array[i][j] = None
                    
                if array[i][j] != None:
                    array[i][j] = int(array[i][j].split()[0])
                    
                    array.append((array[i][j]))
                
            # print(array[i])
            
            
            row_nums = [item for item in array[i] if item is not None]
            row_nums_unduplicated = list(dict.fromkeys(row_nums))
            n = [item for item, count in collections.Counter(row_nums).items() if count > 1]
            
            # print(row_nums)
            # print(row_nums_unduplicated)
            # print(n)
            # print(len(row_nums))     
            # print(len(set(row_nums)))

        for i in range(0, 9):
            for j in range(0, 9):
                puzzle_board_tr[i][j] = puzzle_board[j][i]
            print(puzzle_board_tr[i])

        for i in range(0, 9):
            for j in range(0, 9):
                array_tr[i][j] = array[j][i]
            print(array_tr[i])


        for i in range(0, 9):
            for j in range(0, 9):
                
                
                
                if array[i][j] != puzzle_board[i][j]:
                    # puzzle_board[i][j] = array[i][j]
                    # print(array[i][j])
                    # print(row_nums)
                    # print(row_nums_unduplicated)
                    # for j in range(0, 9):
                    if array[i].count(array[i][j]) > 1:
                        print("hor")
                        red_cell = QLineEdit()
                        self.appearance(red_cell, "incorrect")
                        self.ui.grid_layout.addWidget(red_cell, i, j)
                        red_cell.setText(str(array[i][j]))
                        
                        # break
                    elif array_tr[i].count(array_tr[i][j]) > 1:

                        print("ver")
                        red_cell = QLineEdit()
                        self.appearance(red_cell, "incorrect")
                        self.ui.grid_layout.addWidget(red_cell, i, j)
                        red_cell.setText(str(array_tr[i][j]))
                        # break
                    # if len(row_nums) != len(row_nums_unduplicated):
                            
                    #         # print(j)
                    #         red_cell = QLineEdit()
                    #         self.appearance(red_cell, "incorrect")
                    #         self.ui.grid_layout.addWidget(red_cell, i, j)
                    #         red_cell.setText(str(array[i][j]))
                    #         # print ("❌")
                            
                    #         break
                    # print(array[i])
                    # j = array[i].index(n[0])
                        
            # puzzle_board[i] = array[i]
            

        
           

  
        

    def validation(self, i, j, text):
        # text = self.line_edits[i][j].text()
        if text not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            self.line_edits[i][j].setText("")

        self.check(i, j)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    
    app.exec()