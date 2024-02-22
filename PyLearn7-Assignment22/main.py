import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from main_window import Ui_MainWindow
from database import Database
from functools import partial


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.db = Database()
        self.read_from_database()

        self.ui.btn_new_task.clicked.connect(self.new_task)
        
    def new_task(self):
        
        new_title = self.ui.tbx_new_task_title.text()
        new_description = self.ui.tbx_new_task_description.toPlainText()

        if self.ui.checkbox_important.isChecked():
            new_priority = 1
            self.ui.checkbox_important.setChecked(False)
        else:
            new_priority = 0

        feedback = self.db.add_new_task(new_title, new_description, new_priority)
        if feedback == True:
            
            self.read_from_database()

            self.ui.tbx_new_task_title.setText("")
            self.ui.tbx_new_task_description.setText("")
            
        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکلی رخ داده است.")
            msg_box.exec()

    def read_from_database(self):
        
        for i in reversed(range(self.ui.layout_tasks.count())): 
            self.ui.layout_tasks.itemAt(i).widget().setParent(None)

        tasks = self.db.get_tasks()
        tasks = self.sort_tasks(tasks)
          

        for i in range(len(tasks)):
            new_checkbox = QCheckBox()
            new_label = QLabel()
            new_delet_btn = QPushButton()
            
            
            new_label.setText(tasks[i][1])
            new_delet_btn.setText("❌")
            # new_label_2 = QLabel()
            # new_label_2.setText(tasks[i][2])

            self.ui.layout_tasks.addWidget(new_checkbox, i, 0)
            self.ui.layout_tasks.addWidget(new_label, i, 1)
            self.ui.layout_tasks.addWidget(new_delet_btn, i, 2)
            # self.ui.layout_tasks.addWidget(new_label_2, i ,2)

            if tasks[i][3]==1:
                new_checkbox.setChecked(True)

            
            new_checkbox.toggled.connect(partial(self.check_task, tasks[i][0], new_checkbox))       #A
            new_delet_btn.clicked.connect(partial(self.remove_task, tasks[i][0], [new_checkbox,new_label,new_delet_btn]))    #B
            

    def check_task(self, id, checkbox, x):
        if checkbox.isChecked():
            situation = 1
        else:
            situation = 0
        
        self.db.task_done(id, situation)
        self.read_from_database()
        

    # def priority(self, id, x):
    #     if self.ui.btn_new_task.isChecked():
    #         situation = 1
    #         # print("1")
    #     else:
    #         situation = 0
    #         # print("0")

    #     self.db.task_priority(id, situation)
    #     self.read_from_database()

    def remove_task(self, id, row):
        feedback=self.db.remove_a_task(id)
        if feedback==True:
            for widget in row:
                widget.deleteLater()
        else:
            msg_box = QMessageBox()
            msg_box.setText("مشکلی رخ داده است.")
            msg_box.exec()

    def sort_tasks(self, tasks):
        for task in tasks:
            if task[3]==1:
                tasks.append(tasks.pop(tasks.index(task)))
        print(tasks)
        
        return tasks


        


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()