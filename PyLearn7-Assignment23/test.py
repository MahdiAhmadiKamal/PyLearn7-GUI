from PySide6 import QtCore, QtGui, QtWidgets
# from PySide6.QtCore import QPropertyAnimation, QRectF, QSize, Qt, pyqtProperty
# from PySide6.QtGui import QPainter
# from PySide6.QtWidgets import (
#     QAbstractButton,
#     QApplication,
#     QHBoxLayout,
#     QSizePolicy,
#     QWidget,
# )

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
       MainWindow.setObjectName("MainWindow")
       MainWindow.resize(472, 180)
       self.centralwidget = QtWidgets.QWidget(MainWindow)
       self.centralwidget.setObjectName("centralwidget")
       self.url = QtWidgets.QLineEdit(self.centralwidget)
       self.url.setGeometry(QtCore.QRect(30, 20, 411, 31))
       font = QtGui.QFont()
       font.setFamily("MS Shell Dlg 2")
       font.setPointSize(10)
       font.setBold(True)
       font.setWeight(75)
       self.url.setFont(font)
       self.url.setAutoFillBackground(False)
       self.url.setStyleSheet("border-radius:10px;")
       self.url.setAlignment(QtCore.Qt.AlignCenter)
       self.url.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
       self.url.setObjectName("url")
       MainWindow.setCentralWidget(self.centralwidget)
       self.menubar = QtWidgets.QMenuBar(MainWindow)
       self.menubar.setGeometry(QtCore.QRect(0, 0, 472, 21))
       self.menubar.setObjectName("menubar")
       MainWindow.setMenuBar(self.menubar)
       self.statusbar = QtWidgets.QStatusBar(MainWindow)
       self.statusbar.setObjectName("statusbar")
       MainWindow.setStatusBar(self.statusbar)

       self.retranslateUi(MainWindow)
       QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
       _translate = QtCore.QCoreApplication.translate
       MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
       self.url.setPlaceholderText(_translate("MainWindow", "Playlist URL"))

if __name__ == "__main__":
    import sys
    # main()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())