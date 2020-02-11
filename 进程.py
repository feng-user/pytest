import time
from multiprocessing import Process

# 多进程 就是让 多个cpu 同时 处理 多个任务

def run1():
    for i in range(0, 10):
        print('run1---', i)
        time.sleep(1)


def run2():
    for i in range(0, 10):
        print('run2---', i)
        time.sleep(1)


# run1()
# run2()

if __name__ == '__main__':

    # 创建进程
    p1 = Process(target=run1)
    p2 = Process(target=run2)

    # 执行进程
    p1.start()
    p2.start()