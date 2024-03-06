import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QThread, Signal
from PySide6.QtUiTools import QUiLoader


class MyThread(QThread):

    my_signal = Signal(int)

    def __init__(self):
        super().__init__()
        self.second = 0

    def run(self):
        while True:
            self.second += 1
            # print(self.second)
            self.my_signal.emit(self.second)
            time.sleep(1)

def start_stopwatch():
    thread_stopwatch.start()

def show_number(s):
    window.lbl_stopwatch.setText(str(s))

if __name__ == "__main__":
    

    loader = QUiLoader()
    app = QApplication(sys.argv)
    window = loader.load("mainwindow.ui")
    window.show()

    thread_stopwatch = MyThread()
    window.btn_start_stopwatch.clicked.connect(start_stopwatch)
    thread_stopwatch.my_signal.connect(show_number)

    app.exec()