
first = Node(1)
second = Node(2)
third = Node(3)
#이때까지는 value값만 넣고, Linked는 안 된 상태

first.next = second #second 변수가 참조하는 second 노드 주소값을 넣음
second.next = third
first.value = 6



class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None 
    def append(self, value):
        #먼저, head가 첫 번째 노드를 가리켜야 함
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        #new_node 변수는 마지막 노드를 가리켜야 한다
        else: # self.head가 None이 아닌 경우(즉, 첫 번째 노드는 있는 경우)
            current = self.head
            while current.next:
                current = current.next #다음 칸으로 이동 -> current의 next가 없을 때 까지
            #current next가 없다면
            current.next = new_node #current.next가 없을 때, 즉 마지막 노드일 때 new_node(마지막 노드) 추가
    def get(self, idx):
        #LinkedList는 head로부터 시작해서 노드에 접근!
        current = self.head
        #원하는 인덱스로 이동 current.next이용 when? idx값 만큼
        for _ in range(idx):
            current = current.next
        #다 이동했으면 값 반환
        return current.value

        
        
    def insert(self, idx, value):
        pass
    def delete(self, idx):
        pass