import time


class Fei:

    def __init__(self):
        self.a = 1
        self.b = 0

    def __iter__(self):
        return self

    def __next__(self):

        self.a, self.b = self.a + self.b, self.a

        return self.b



for i in Fei():
    print(i)
    time.sleep(1)