# import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
import math


def clean():
    main_window.txtbox.setText("")

def point():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + ".")

def num_0():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + "0")

def num_1():
    e = main_window.txtbox.text()           # to read textbox
    main_window.txtbox.setText(e + "1")     # to write in textbox

def num_2():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + "2")

def num_3():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + "3")

def num_4():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + "4")

def num_5():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + "5")

def num_6():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + "6")  

def num_7():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + "7")

def num_8():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + "8")

def num_9():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + "9")

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

def percent():
    b = float(main_window.txtbox.text())
    c = (a/b)*100
    main_window.txtbox.setText(str(c))

def sin():
    rad = float(main_window.txtbox.text())*math.pi/180
    a = math.sin(rad)
    main_window.txtbox.setText(str(a))


def cos():
    rad = float(main_window.txtbox.text())*math.pi/180
    a = math.cos(rad)
    main_window.txtbox.setText(str(a))

def tan():
    rad = float(main_window.txtbox.text())*math.pi/180
    if rad == 90*math.pi/180:
        main_window.txtbox.setText("It is undefined.")
    else:
        a = math.tan(rad)
        main_window.txtbox.setText(str(a))

def cot():
    rad = float(main_window.txtbox.text())*math.pi/180
    if rad == 0:
        main_window.txtbox.setText("It is undefined.")
    else:
        a = 1/(math.tan(rad))
        main_window.txtbox.setText(str(a))

def log():
    a = float(main_window.txtbox.text())
    if a < 0:
        main_window.txtbox.setText("It is undefined.")
    else:
        b = math.log10(a)
        main_window.txtbox.setText(str(b))

def sqrt():
    a = float(main_window.txtbox.text())
    if a < 0:
        main_window.txtbox.setText("It is undefined.")
    else:
        b = math.sqrt(a)
        main_window.txtbox.setText(str(b))

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
            main_window.txtbox.setText("It is undefined.")


    main_window.txtbox.setText(str(c))

loader = QUiLoader()
app = QApplication([])
main_window = loader.load("main.ui")
main_window.show()


main_window.btn_clean.clicked.connect(clean)
main_window.btn_point.clicked.connect(point)
main_window.btn_0.clicked.connect(num_0)     # to connect the key to its function
main_window.btn_1.clicked.connect(num_1)
main_window.btn_2.clicked.connect(num_2)
main_window.btn_3.clicked.connect(num_3)
main_window.btn_4.clicked.connect(num_4)
main_window.btn_5.clicked.connect(num_5)
main_window.btn_6.clicked.connect(num_6)
main_window.btn_7.clicked.connect(num_7)
main_window.btn_8.clicked.connect(num_8)
main_window.btn_9.clicked.connect(num_9)
main_window.btn_sum.clicked.connect(sum)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_mul.clicked.connect(mul)
main_window.btn_div.clicked.connect(div)
main_window.btn_percent.clicked.connect(percent)
main_window.btn_sin.clicked.connect(sin)
main_window.btn_cos.clicked.connect(cos)
main_window.btn_tan.clicked.connect(tan)
main_window.btn_cot.clicked.connect(cot)
main_window.btn_log.clicked.connect(log)
main_window.btn_sqrt.clicked.connect(sqrt)
main_window.btn_equal.clicked.connect(result)

app.exec()