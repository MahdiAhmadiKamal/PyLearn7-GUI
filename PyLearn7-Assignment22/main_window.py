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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateTimeEdit, QGridLayout,
    QHBoxLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(478, 519)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.layout_tasks = QGridLayout()
        self.layout_tasks.setObjectName(u"layout_tasks")

        self.verticalLayout.addLayout(self.layout_tasks)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tbx_new_task_title = QLineEdit(self.centralwidget)
        self.tbx_new_task_title.setObjectName(u"tbx_new_task_title")

        self.horizontalLayout.addWidget(self.tbx_new_task_title)

        self.btn_new_task = QPushButton(self.centralwidget)
        self.btn_new_task.setObjectName(u"btn_new_task")
        self.btn_new_task.setMinimumSize(QSize(30, 30))
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setPointSize(24)
        font.setBold(False)
        self.btn_new_task.setFont(font)
        self.btn_new_task.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.btn_new_task)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bx_date_time = QDateTimeEdit(self.centralwidget)
        self.bx_date_time.setObjectName(u"bx_date_time")

        self.horizontalLayout_2.addWidget(self.bx_date_time)

        self.checkbox_important = QCheckBox(self.centralwidget)
        self.checkbox_important.setObjectName(u"checkbox_important")

        self.horizontalLayout_2.addWidget(self.checkbox_important)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.tbx_new_task_description = QTextEdit(self.centralwidget)
        self.tbx_new_task_description.setObjectName(u"tbx_new_task_description")

        self.verticalLayout.addWidget(self.tbx_new_task_description)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 478, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_new_task.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.checkbox_important.setText(QCoreApplication.translate("MainWindow", u"important", None))
    # retranslateUi

