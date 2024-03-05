import threading
import time


def test(name):
    for i in range(5):
        print(name)
        time.sleep(0.5)

t1 = threading.Thread(target=test, args=["Ali"])
t2 = threading.Thread(target=test, args=["Mahdi"])

t1.start()
t2.start()