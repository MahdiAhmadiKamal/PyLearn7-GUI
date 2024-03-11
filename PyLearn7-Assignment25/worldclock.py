import time
import pytz
from datetime import datetime
from PySide6.QtCore import QThread, Signal
from mytime import MyTime

class WorldClockThread(QThread):
    signal_show = Signal(MyTime)
    def __init__(self):
        super().__init__()

    def run(self):
        while True:

            iran_time = pytz.timezone('Asia/Tehran')
            self.iran_time_str = datetime.now(iran_time).strftime('%H:%M:%S')        

            germany_time = pytz.timezone('Europe/Berlin')
            self.germany_time_str = datetime.now(germany_time).strftime('%H:%M:%S')

            usa_time=pytz.timezone('US/Eastern')
            self.usa_time_str = datetime.now(usa_time).strftime('%H:%M:%S')

            time.sleep(1)
            self.signal_show.emit([self.iran_time_str, self.germany_time_str, self.usa_time_str])