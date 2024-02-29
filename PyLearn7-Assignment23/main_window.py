# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(501, 541)
        self.menu_new = QAction(MainWindow)
        self.menu_new.setObjectName(u"menu_new")
        self.menu_open_file = QAction(MainWindow)
        self.menu_open_file.setObjectName(u"menu_open_file")
        self.menu_puzzle_answer = QAction(MainWindow)
        self.menu_puzzle_answer.setObjectName(u"menu_puzzle_answer")
        self.menu_about = QAction(MainWindow)
        self.menu_about.setObjectName(u"menu_about")
        self.menu_exit = QAction(MainWindow)
        self.menu_exit.setObjectName(u"menu_exit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 10, 451, 441))
        self.grid_layout = QGridLayout(self.gridLayoutWidget)
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.btn_dark_light_mode = QPushButton(self.centralwidget)
        self.btn_dark_light_mode.setObjectName(u"btn_dark_light_mode")
        self.btn_dark_light_mode.setGeometry(QRect(20, 460, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 501, 22))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.menu_new)
        self.menuGame.addAction(self.menu_open_file)
        self.menuGame.addAction(self.menu_puzzle_answer)
        self.menuGame.addAction(self.menu_about)
        self.menuGame.addAction(self.menu_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sudoku Game", None))
        self.menu_new.setText(QCoreApplication.translate("MainWindow", u"New...", None))
        self.menu_open_file.setText(QCoreApplication.translate("MainWindow", u"Open File...", None))
        self.menu_puzzle_answer.setText(QCoreApplication.translate("MainWindow", u"Puzzle Answer", None))
        self.menu_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.menu_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_dark_light_mode.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.menuGame.setTitle(QCoreApplication.translate("MainWindow", u"Game", None))
    # retranslateUi

