class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)
        
    def move_up(self, inserted_idx):        #루트노드라 바꿀 필요가 없는지, 아니면 바꿀 필요가 있는지 판단하는 METHOD
        if inserted_idx <= 1:               #루트노드이면 더이상 할게 없으니 여기서 FALSE임
            return False
        
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False
        
    def insert(self, data):                 #루트노드에 있냐, 아니면 루트노드가 아닌데 부모노드의 값과 비교후 위치 변경 METHOD
        if len(self.heap_array) == 0:       #완전 이진 트리에 맞춰서 배열에 데이터를 넣은 것! APPEND로 맨끝에 데이터 추가
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        
        inserted_idx = len(self.heap_array) - 1 #지금들어간 index의 번호를 알아야 함. 배열의 길이에 -1을 해야 함. 0는 없는 것으로함
                                                #전체index번호를 구함
        while self.move_up(inserted_idx):      #간단하게 SWAP을 해서 부모와 자식을 바꾸는 처리가 이루어짐
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx           #INSERT를 한게 PARENT의 위치로 감. INSERT INDEX를 PARENT INDEX로 바꿔준것 뿐!
        
        return True

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)