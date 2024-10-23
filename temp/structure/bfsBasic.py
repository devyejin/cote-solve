#root 노드부터 전체를 방문
def bfs(root):
    visited = [] #방문 기록용
    if root is None:
        return 0:
    q = deque() #FIFO 구조니까 deque 필요
    q.append(root) # 시작점 deque에 넣고 시작
    
    while q: #q가 비면 false 반환
        cur_node = q.popleft()
        visited.append(cur_node.value) #방문 기록
        
        if cur_node.left:
            q.append(cur_node.left)
        if cur_node.right:
            q.append(cur_node.right)
        return visited

bfs(root)