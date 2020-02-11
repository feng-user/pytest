# 生成器是一个特殊的迭代器
# 可以用for循环执行，可以用next执行
# 如果一个方法中包含 yield ，那么这个方法就是一个生成器

def foo():
    print(1)
    yield 2   # yield 返回当前值，并保存当前的执行的位置，等待下一次next执行，那么从当前位置在 往下执行
    print(3)
    yield 4
    print(5)


# for i in foo():
#     print(i)

# f = foo()
# print(next(f))
# print(next(f))
# print(next(f))


