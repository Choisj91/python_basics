# 간단한 링크드 리스트 EXAMPLE

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# 링크드 리스트로 데이터 추가하기
def add(data):
    node = head
    while node.next:           #node의 next가 있으면, 다음 주소가 저장되어 있으면 다음 node의 주소로 이동하고, 또다시 그 다음 주소로 이동
        node = node.next
    node.next = Node(data)     #마지막 Node의 주소에 지금 생성한 node가 늘 가르키게 하기 때문에 결과적으로 전체 링크드인 리스트에 맨끝에 새로운 노드를 연결


# Node와 Node 연결하기(포인터 활용)
# 가장 앞의 노드를 알아두기 위해서 별도의 변수를 써서 head라고 선언해서 가장 앞의 주소를 알게 된다
node1 = Node(1)
head  = node1       # 가장 맨 앞의 node를 미리 알고, 별도의 변수를 써서 node1의 값을 가진 head선언
# node2 = Node(2)
# node1.next = node2 # 주소가 연결되서 node2를 가르키는 형태가 됨

for index in range(2,10):
    add(index)

# 순회하면서.. 이동하면서 포인터로 연결이되서 데이터를 하나씩 순회해서 다음 데이터의 출력을 확인 가능
# node = head
# while node.next:
#     print(node.data)
#     node = node.next
# print(node.data)

node3 = Node(1.5)

node = head
search = True
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next
        
node_next = node.next
node.next = node3
node3.next = node_next

node = head
while node.next:
    print(node.data)
    node = node.next
print(node.data)


