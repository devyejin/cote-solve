#Binary Tree는 Node로 구현하니까 먼저 Node부터 정의
class Node:
    def __init__(self) -> None:
        self.value = 0
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None

bt = BinaryTree() #노드만 생성
bt.root = Node(value = 1) # root에 노드를 연결
bt.root.left = Node(value = 2) # left child 연결
bt.roof.right = Node(value = 3)
bt.root.left.left = Node(value = 4)
bt.root.left.right = Node(value = 5)
bt.root.right.right  = Node(value = 6)