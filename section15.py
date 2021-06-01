#STACK
# 함수 안에서 자기 함수를 부르는 것이다
# 재귀 함수(자기 함수 안에서 함수를 호출하는 것)
# def recursive(data):
#     if data < 0:
#         print("ended")
#     else:
#         print(data)
#         recursive(data-1)
#         print("returned",data)

# recursive(4)

#data_stack
# data_stack = list()

# data_stack.append('1')
# data_stack.append('2')

# print(data_stack)
# print(len(data_stack))

# data_stack.pop()

# print(data_stack)
# print(len(data_stack))

# 연습1: 리스트 변수로 스택을 다루는 pop, push 기능 구현해보기 (pop, push 함수 사용하지 않고 직접 구현해보기)
data_stack = list()

def pushs(data):
    data_stack.append(data)

def pops():
    data = data_stack[-1]
    del data_stack[-1]
    return data

for index in range(0,20,2):
    pushs(index)

print(data_stack)
print(len(data_stack))
pops()
print(data_stack)
print(len(data_stack))
