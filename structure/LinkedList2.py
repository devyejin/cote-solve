#Node는 value(데이터 값)과 next(다음 노드의 주소값)으로 구성
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next 
        
#head는 LinkedList의 첫 번쨰 노드를 가리킴
#LinkedList의 생성 초기에는 노드가 없음
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def append(self, value):
        #노드 생성
        new_node = Node(value)
        if self.head is None: #첫 번째 노드인 경우
            self.head = new_node
            self.tail = new_node
        else:
            #두 번째 이상의 노드인 경우, tail은 마지막 노드를 가리키도록
            self.tail.next = new_node #이전값이랑 연결
            #tail값 업데이트
            self.tail = new_node #tail을 마지막 노드로 이동
    
    
        #O(1), tail 이용
    def append_v2(self, value): 
        new_node = Node(value)
        
        #idx = 0 인 경우
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        #idx != 0 인 경우
        else:
            #tail(기존 마지막값)의 next에 new_node 연결
            self.tail.next = new_node
            #tail을 추가된 node로 이동(마지막화) -> 끝
            self.tail = new_node                                                                                                                                                                                                                  
    
    
    
    def get(self, idx):
        #LinkedList는 head노드로부터 시작
        current = self.head
        #원하는 위치로 current를 이동, 언제까지? idx까지
        for _ in range(idx):
            current = current.next
        #이동 끝났으면 값 반환
        return current.value
    
    
    def insert(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    
    
    def insert(self, idx, value):
        #노드 생성
        new_node = Node(value)
        
        #case ids = 0
        if idx == 0:
            new_node.next = self.head #기존 idx=0노드를 가리킬 수 있도록
            self.head = new_node #head 이동
        
        
        #case idx != 0
        else:
            current = self.head
            #current를 idx-1까지 이동
            for _ in range(idx-1):
                current = current.next
            new_node.next = current.next # 1번 
            current.next = new_node #2번
            
    def remove(self, idx):
        if idx == 0:
            self.head = self.head.next
        
        else:
            current = self.head
            for _ in range(idx-1):
                current = current.next
            current.next = current.next.next
    

        
        
            
#데이터로 디버깅하며 검증
li = LinkedList()
li.append(0)
li.append(1)
li.append(2)
li.append(3)



print(li.get(2))