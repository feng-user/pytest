from queue import Queue

# q就是先进先出队列
q = Queue()

q.put('a')
q.put('b')
q.put('c')

print(q.get())

print(q.empty())

print(q.get())
print(q.get())

