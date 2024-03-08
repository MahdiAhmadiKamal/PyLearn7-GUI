import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QThread, Signal
from mytime import MyTime
from mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Stopwatch
        self.thread_stopwatch = StopwatchThread()
        self.thread_stopwatch.signal_show.connect(self.show_time_stopwatch)
        self.ui.lbl_stopwatch.setText("0:0:0")
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_reset_stopwatch.clicked.connect(self.reset_stopwatch)
        
        #Timer
        self.h = int(self.ui.tbx_hour_timer.text())
        self.m = int(self.ui.tbx_minute_timer.text())
        self.s = int(self.ui.tbx_second_timer.text())

        self.thread_timer = TimerThread(self.h, self.m, self.s)
        # self.t = MyTime(self.h, self.m, self.s)
        # self.show_time_timer(self.t)

        
        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        self.ui.btn_reset_timer.clicked.connect(self.reset_timer)
        self.thread_timer.signal_show.connect(self.show_time_timer)
        

    def show_time_stopwatch(self, time):
        self.ui.lbl_stopwatch.setText(f"{time.hour}:{time.minute}:{time.second}")

    def start_stopwatch(self):
        self.thread_stopwatch.start()

    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    def reset_stopwatch(self):
        self.thread_stopwatch.reset()
        self.ui.lbl_stopwatch.setText("0:0:0")


    def show_time_timer(self, time):
        self.ui.tbx_hour_timer.setText(f"{time.hour}")
        self.ui.tbx_minute_timer.setText(f"{time.minute}")
        self.ui.tbx_second_timer.setText(f"{time.second}")
        if time.hour == time.minute == time.second == 0:
            self.thread_timer.terminate()
            
            msg = QMessageBox()
            msg.setText('Timer done')
            msg.exec()
            

    def start_timer(self):
        hour = int(self.ui.tbx_hour_timer.text())
        minute = int(self.ui.tbx_minute_timer.text())             
        second = int(self.ui.tbx_second_timer.text())
        self.thread_timer.get(hour,minute,second)
        self.thread_timer.start()

    def stop_timer(self):
        self.thread_timer.terminate()

    def reset_timer(self):
        self.thread_timer.reset()
        self.ui.tbx_hour_timer.setText(str(self.thread_timer.time.hour))
        self.ui.tbx_minute_timer.setText(str(self.thread_timer.time.minute))
        self.ui.tbx_second_timer.setText(str(self.thread_timer.time.second)) 


    
class TimerThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self, h, m, s):
        super().__init__()
        
        self.hh = h 
        self.mm = m
        self.ss = s
        self.time = MyTime(self.hh, self.mm, self.ss)
        

    def run(self):
        while True:
            self.time.minus()
            # print(self.second)
            self.signal_show.emit(self.time)
            time.sleep(1)
            

    def reset(self):
        self.time.hour =  0
        self.time.minute = 15
        self.time.second = 10
        self.signal_show.emit(self.time)

    def get(self , hour , minute , second):
        self.time.second = second
        self.time.minute = minute 
        self.time.hour = hour
        

class StopwatchThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0, 0, 0)

    def run(self):
        while True:
            self.time.plus()
            # print(self.second)
            self.signal_show.emit(self.time)
            time.sleep(1)

    def reset(self):
        self.time.hour = 0
        self.time.minute = 0
        self.time.second = 0
        





if __name__ == "__main__":
    

    # loader = QUiLoader()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    

    app.exec()