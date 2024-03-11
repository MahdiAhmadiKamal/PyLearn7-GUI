import time
from PySide6.QtCore import QThread, Signal


class AlarmThread(QThread):
    signal_show = Signal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            self.time = time
            self.now = self.time.strftime('%I:%M:%S')
            self.signal_show.emit(self.now) 
            time.sleep(1)