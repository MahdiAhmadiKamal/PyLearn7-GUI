import sys
from PySide6.QtCore import * 
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()

        url = QLineEdit()
        save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")

        layout.addWidget(url)
        layout.addWidget(save_location)
        layout.addWidget(progress)
        layout.addWidget(download)

        self.setLayout(layout)
             
             
app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec()