'''
# 迭代对象
# 可用于 for 循环的都是 可迭代对象
from collections import Iterable

a = '12345'
b = [1,2,3]
c = 12

# print(isinstance(a, str))
# print(isinstance(b, list))

print(isinstance(a, Iterable))
print(isinstance(b, Iterable))
print(isinstance(c, Iterable))
'''


from collections import Iterable, Iterator

# b = iter([1,2,3])
# print(isinstance(b, Iterator))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))


# 迭代器
# for i in Range():
#     print(i) # 1,2,3,4,5..10


# 1 1 2 3 5 8
class Range():

    def __init__(self, end, start=0, step=1):
        if start == 0:
            self.start = start
            self.end = end
        else:
            self.start = end
            self.end = start
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):

        current = self.start

        if current >= self.end:
            raise StopIteration

        self.start += self.step

        return current




for i in Range():
    print(i)

# 迭代器只会把当前的结果保存在内存中
# for i in Range():
#     print(i) # 100


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a = [i for i in range(10000000)]
#
# print(a.__sizeof__())
# print(Range().__sizeof__())
