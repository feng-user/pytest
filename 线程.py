import time
from threading import Thread

def run1():
    for i in range(0, 10):
        print('run1---',i)
        time.sleep(1)

def run2():
    for i in range(0, 10):
        print('run2---',i)
        time.sleep(1)

if __name__ == '__main__':

    # 创建线程
    t1 = Thread(target=run1)
    t2 = Thread(target=run2)

    t1.start()
    t2.start()
