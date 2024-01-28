from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader


def button_1():
    main_window.txtbox.setText("1")

def button_2():
    main_window.txtbox.setText("2")


def sum():
    global a
    global operator
    a = float(main_window.txtbox.text())
    operator = "+"
    main_window.txtbox.setText("")

def sub():
    global a
    global operator
    a = float(main_window.txtbox.text())
    operator = "-"
    main_window.txtbox.setText("")

def mul():
    global a
    global operator
    a = float(main_window.txtbox.text())
    operator = "*"
    main_window.txtbox.setText("")

def div():
    global a
    global operator
    a = float(main_window.txtbox.text())
    operator = "/"
    main_window.txtbox.setText("")

def result():
    b = float(main_window.txtbox.text())
    if operator == "+":
        c = a+b
    elif operator == "-":
        c = a-b
    elif operator == "*":
        c = a*b
    elif operator == "/":
        if b!=0:
            c = a/b
        elif b==0:
            main_window.txtbox.setText("cannot devide by zero")


    main_window.txtbox.setText(str(c))

loader = QUiLoader()
app = QApplication([])
main_window = loader.load("main.ui")
main_window.show()

main_window.btn_1.clicked.connect(button_1)
main_window.btn_2.clicked.connect(button_2)
main_window.btn_sum.clicked.connect(sum)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_mul.clicked.connect(mul)
main_window.btn_div.clicked.connect(div)
main_window.btn_equal.clicked.connect(result)

app.exec()