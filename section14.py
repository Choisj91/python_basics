import queue

# FIFO
data_queue = queue.Queue()

data_queue.put("Fun Coding")
data_queue.put("Hello World")

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())
print(data_queue.qsize())

# LIFO
data_queue = queue.LifoQueue()

data_queue.put("python")
data_queue.put("java")
data_queue.put("php")

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())
print(data_queue.get())
print(data_queue.qsize())

# PriorityQueue : tuple의 형태로 쌍으로 넣게 되어 있음
data_queue = queue.PriorityQueue()

data_queue.put((3,"Japan"))
data_queue.put((1,"South Korea"))
data_queue.put((2,"England"))

print(data_queue.qsize())
print(data_queue.get())
print(data_queue.get())
print(data_queue.get())
print(data_queue.qsize())

# 연습1: 리스트 변수로 큐를 다루는 enqueue, dequeue 기능 구현해보기
queue_list = list()

def enqueue(data):
    queue_list.append(data)

def dequeue():
    data = queue_list[0]
    del queue_list[0]
    return data

for index in range(10):
    enqueue(index)

print(queue_list)
print(len(queue_list))
dequeue()
print(queue_list)
print(len(queue_list))
