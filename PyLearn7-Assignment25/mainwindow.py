# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(664, 540)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(50, 20, 551, 461))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.btn_germany_worldclock = QPushButton(self.tab)
        self.btn_germany_worldclock.setObjectName(u"btn_germany_worldclock")
        self.btn_germany_worldclock.setGeometry(QRect(230, 250, 75, 24))
        self.btn_usa_worldclock = QPushButton(self.tab)
        self.btn_usa_worldclock.setObjectName(u"btn_usa_worldclock")
        self.btn_usa_worldclock.setGeometry(QRect(320, 250, 75, 24))
        self.btn_iran_worldclock = QPushButton(self.tab)
        self.btn_iran_worldclock.setObjectName(u"btn_iran_worldclock")
        self.btn_iran_worldclock.setGeometry(QRect(130, 250, 75, 24))
        self.lbl_worldclock = QLabel(self.tab)
        self.lbl_worldclock.setObjectName(u"lbl_worldclock")
        self.lbl_worldclock.setGeometry(QRect(150, 90, 231, 71))
        font = QFont()
        font.setFamilies([u"Seven Segment"])
        font.setPointSize(50)
        self.lbl_worldclock.setFont(font)
        self.lbl_worldclock.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.lbl_stopwatch = QLabel(self.tab_3)
        self.lbl_stopwatch.setObjectName(u"lbl_stopwatch")
        self.lbl_stopwatch.setGeometry(QRect(160, 90, 231, 71))
        self.lbl_stopwatch.setFont(font)
        self.lbl_stopwatch.setAlignment(Qt.AlignCenter)
        self.btn_start_stopwatch = QPushButton(self.tab_3)
        self.btn_start_stopwatch.setObjectName(u"btn_start_stopwatch")
        self.btn_start_stopwatch.setGeometry(QRect(140, 250, 75, 24))
        self.btn_stop_stopwatch = QPushButton(self.tab_3)
        self.btn_stop_stopwatch.setObjectName(u"btn_stop_stopwatch")
        self.btn_stop_stopwatch.setGeometry(QRect(240, 250, 75, 24))
        self.btn_reset_stopwatch = QPushButton(self.tab_3)
        self.btn_reset_stopwatch.setObjectName(u"btn_reset_stopwatch")
        self.btn_reset_stopwatch.setGeometry(QRect(330, 250, 75, 24))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tbx_hour_timer = QLineEdit(self.tab_4)
        self.tbx_hour_timer.setObjectName(u"tbx_hour_timer")
        self.tbx_hour_timer.setGeometry(QRect(170, 90, 61, 71))
        font1 = QFont()
        font1.setFamilies([u"Seven Segment"])
        font1.setPointSize(30)
        self.tbx_hour_timer.setFont(font1)
        self.tbx_hour_timer.setAlignment(Qt.AlignCenter)
        self.tbx_minute_timer = QLineEdit(self.tab_4)
        self.tbx_minute_timer.setObjectName(u"tbx_minute_timer")
        self.tbx_minute_timer.setGeometry(QRect(240, 90, 61, 71))
        self.tbx_minute_timer.setFont(font1)
        self.tbx_minute_timer.setAlignment(Qt.AlignCenter)
        self.tbx_second_timer = QLineEdit(self.tab_4)
        self.tbx_second_timer.setObjectName(u"tbx_second_timer")
        self.tbx_second_timer.setGeometry(QRect(310, 90, 61, 71))
        self.tbx_second_timer.setFont(font1)
        self.tbx_second_timer.setAlignment(Qt.AlignCenter)
        self.btn_reset_timer = QPushButton(self.tab_4)
        self.btn_reset_timer.setObjectName(u"btn_reset_timer")
        self.btn_reset_timer.setGeometry(QRect(330, 210, 75, 24))
        self.btn_stop_timer = QPushButton(self.tab_4)
        self.btn_stop_timer.setObjectName(u"btn_stop_timer")
        self.btn_stop_timer.setGeometry(QRect(240, 210, 75, 24))
        self.btn_start_timer = QPushButton(self.tab_4)
        self.btn_start_timer.setObjectName(u"btn_start_timer")
        self.btn_start_timer.setGeometry(QRect(140, 210, 75, 24))
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 664, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_germany_worldclock.setText(QCoreApplication.translate("MainWindow", u"Germany", None))
        self.btn_usa_worldclock.setText(QCoreApplication.translate("MainWindow", u"USA", None))
        self.btn_iran_worldclock.setText(QCoreApplication.translate("MainWindow", u"Iran", None))
        self.lbl_worldclock.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"World Clock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Alarm", None))
        self.lbl_stopwatch.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_start_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stop_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_reset_stopwatch.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Stopwatch", None))
        self.tbx_hour_timer.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tbx_minute_timer.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.tbx_second_timer.setText(QCoreApplication.translate("MainWindow", u"10", None))
        self.btn_reset_timer.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btn_stop_timer.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btn_start_timer.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Timer", None))
    # retranslateUi

