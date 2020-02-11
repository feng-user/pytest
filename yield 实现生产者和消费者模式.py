# 生产者
import time


def sends(f):

    f.send(None)

    num = 1

    while True:

        print(f'做了{num}个包子')

        f.send(num)

        num += 1

        time.sleep(1)




# 消费者
def Pay():

    while True:

        num = yield

        print(f'吃了{num}个包子')


f = Pay()
sends(f)