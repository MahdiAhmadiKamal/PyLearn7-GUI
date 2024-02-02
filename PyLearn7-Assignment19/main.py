import sys
import random
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
from function import non_repeating_random_2D_array


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.buttons = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3, self.ui.btn_4],
                        [self.ui.btn_5, self.ui.btn_6, self.ui.btn_7, self.ui.btn_8],
                        [self.ui.btn_9, self.ui.btn_10, self.ui.btn_11, self.ui.btn_12],
                        [self.ui.btn_13, self.ui.btn_14, self.ui.btn_15, self.ui.btn_16]]

        my_list = non_repeating_random_2D_array(4, 4)
        for i in range (4):
            for j in range (4):
                r = my_list[i][j]
                self.buttons[i][j].setText(str(r))
        print(r)               
        
app = QApplication(sys.argv)

main_window = MainWindow()
main_window.show()

app.exec()