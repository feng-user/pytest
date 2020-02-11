# 进程之间数据共享有三种方式，队列 queue  管道 pipe  管理器 manager

from multiprocessing import Process, Manager

def run1(lis):
    lis.append('run1')


def run2(lis):
    lis.append('run2')


if __name__ == '__main__':

    with Manager() as manager:

        lis = manager.list()

        # 创建进程
        p1 = Process(target=run1, args=(lis,))
        p2 = Process(target=run2, args=(lis,))

        # 执行进程
        p1.start()
        p2.start()


        # 主线程 必须等待 自线程全部执行完之后，在结束
        p1.join()
        p2.join()

        print(lis)