# 一、用一行代码实现变量a和b的数值交换： a = 1  b = 2
'''
a = 1
b = 2

# c = a
# a = b
# b = c

a, b = b, a

print(a, b)
'''

'''
# 斐波那契额数列
# 1 1 2 3 5 8 13 21 34
a = 1
b = 1

while True:
    print(b)
    a, b = a+b, a
    if b > 34:
        break
'''

# 二、定义一个方法f，使其能接收所有格式的参数
# def show(*args, **kwargs):
#     pass


# 五、请用一行代码去掉列表[2,12,10,2,33,12,20]中重复的值
# a = [2,12,10,2,33,12,20]
# a = set(a)
# print(list(a))


'''
# 六
def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
    print(l)


f(2)  # [0, 1]
f(3, [3, 2, 1])  # [3,2,1,0,1,4]
f(3)  # [0, 1, 0, 1, 4]
'''

'''
# 七、用map方法和列表推导式把['aa','bb','cc']变成['a','b','c']
a = ['aa', 'bb', 'cc']
# a = map(lambda x: x[0], a)
# print(list(a))

a = [i[0] for i in a]
print(a)
'''

'''
# 八、找到字典中得分最高的人的名字的方法
d = {'ben': 20, 'lili': 32, 'lucy': 16, 'mark': 28}
# d = [
#     {'name': 'a', 'age': 20},
#     {'name': 'b', 'age': 10},
#     {'name': 'c', 'age': 30},
# ]
m = max(d, key=lambda x: d.get(x))
print(m)

# lis = d.values()
# m = max(lis)
# for k, v in d.items():
#     if v == m:
#         print(k)
#         break
'''

# 九、请用冒泡排序使列表a=[12,33,6,3,18,24]从大到小排序

a = [12, 33, 6, 3, 18, 24]

''' 冒泡排序
for i in range(0, len(a)-1):
	for j in range(0, len(a)-1-i):
		if a[j] < a[j+1]:
			a[j], a[j+1] = a[j+1], a[j]
'''

''' 选择排序
for i in range(0, len(a)-1):
	for j in range(i+1, len(a)):
		if a[i] < a[j]:
			a[i], a[j] = a[j], a[i]
'''

# print(a)


'''
# 请写一个装饰器，执行此函数并打印函数执行的时间
def outer(func):
    def inner(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
    return inner

@outer
def f(a):
    for i in range(0, a):
        i += 1
    print(i)


f(1000000)
'''

'''
# 十一、深复制和浅复制的区别是什么
from copy import deepcopy

a = [1, 2, [11, 22]]
b = a.copy()  # 浅复制: 只把列表中第一层的数据 重新 放入一个新的内存中， 嵌套的列表还是用之前的 内存地址
c = deepcopy(a)  # 深复制: 把 列表中 所有的值 全部复制到 一块新的 内存中
a[0] = 11
a[2][0] = 111
print(a)
print(b)
print(c)
'''

'''
# 十二、定义一个类，用__new__方法写出单例模式
class A(object):

    instance = None

    def __new__(cls, *args, **kwargs):

        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance


a = A()
b = A()
c = A()
print(id(a))
print(id(b))
print(id(c))
'''






'''
class P():
    def __init__(self):
        self.num = 100

    def show(self):
        print(self.num)

class S(P):
    def show(self):
        super().show()
        print(S.__name__)

s = S()
s.show()
'''




'''
class A:
    __name = 'abc'

print(A._A__name)
'''



'''
class Student:


    name = 'ben'


    def show(self):
        pass

    @staticmethod
    def getname():
        pass

    @classmethod
    def getage(cls):
        print(cls.name)

Student.getage()
'''








# 删除 索引是 偶数 的列表元素
a = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c']


# data = []
# for k,v in enumerate(a):
#     if k % 2 != 0:
#         data.append(v)
#
# print(data)



# for i in range(len(a)-1, -1, -1):
#     if i % 2 == 0:
#         del a[i]



# a = [v for k, v in enumerate(a) if k % 2 != 0]
#
# print(a)

# for i in b:
#     a.remove(i)
#
# print(a)





# a = [10,20,12,8,30]
# a.sort()     # 没有返回值，针对 原列表
# b = sorted(a)  # 返回一个新的列表

# print(b)







num = input('请输入数字:')

def do1():
    print('i am do1')

def do2():
    print('i am do2')

def do3():
    print('i am do3')

def do4():
    print('i am do4')

dic = {'1':do1, '2':do2, '3':do3}

dic.get(num, do4)()