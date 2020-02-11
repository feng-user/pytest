def Fib():
    a = 1
    b = 0
    while True:
        a, b = a+b, a
        if b > 13:
            break
        num = yield b  # return b
        print('----',num)


# 生成器可以被 for 循环执行，next 执行，也可以被 send 执行
f = Fib()
print(f.send(None))
print(f.send(1))
print(f.send(2))
print(f.send(3))







# for i in Fib():
#     print(i)
# f = Fib()
# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))