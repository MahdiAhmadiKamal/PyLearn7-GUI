import time
from PySide6.QtCore import QThread, Signal
from mytime import MyTime


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