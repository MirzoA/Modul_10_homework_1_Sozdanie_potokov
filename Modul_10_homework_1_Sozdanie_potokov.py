import threading
import time
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def function1():
    for i in range(1,11):
        print(i)
        time.sleep(1)

def function2():
    for i in abc:
        print(i)
        time.sleep(1.1)

th1 = threading.Thread(target=function1)
th2 = threading.Thread(target=function2)

th1.start()
th2.start()

th1.join()
th2.join()