import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
# import math


def clean():
    main_window.txtbox.setText("")

def point():
    e = main_window.txtbox.text()
    main_window.txtbox.setText(e + ".")

def num(x):
    old_num = main_window.txtbox.text()
    new_num = old_num + x
    main_window.txtbox.setText(new_num)

def sum():
    global a
    global operator
    a = float(main_window.txtbox.text())
    operator = "+"
    main_window.txtbox.setText("")

def sub():
    global a
    global operator
    try:
        a = float(main_window.txtbox.text())
        operator = "-"
        main_window.txtbox.setText("")
    except(ValueError):
        main_window.txtbox.setText("-")

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
            c = "It is undefined."

    main_window.txtbox.setText(str(c))

loader = QUiLoader()
app = QApplication([])
main_window = loader.load("main.ui")
main_window.show()


main_window.btn_clean.clicked.connect(clean)
main_window.btn_point.clicked.connect(point)

main_window.btn_0.clicked.connect(partial(num, "0"))    # to connect the key to its function
main_window.btn_1.clicked.connect(partial(num, "1"))
main_window.btn_2.clicked.connect(partial(num, "2"))
main_window.btn_3.clicked.connect(partial(num, "3"))
main_window.btn_4.clicked.connect(partial(num, "4"))
main_window.btn_5.clicked.connect(partial(num, "5"))
main_window.btn_6.clicked.connect(partial(num, "6"))
main_window.btn_7.clicked.connect(partial(num, "7"))
main_window.btn_8.clicked.connect(partial(num, "8"))
main_window.btn_9.clicked.connect(partial(num, "9"))

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