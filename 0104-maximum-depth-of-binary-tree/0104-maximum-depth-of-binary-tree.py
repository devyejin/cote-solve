class Solution:
    def maxDepth(self, root) -> int:
        #visited = [] #방문 기록용 => 현재 depth 기록용이 필요함
        max_depth = 0
        if root is None:
            return max_depth #아무것도 없다면, depth 0
        
        q = deque() #예약용
        q.append((root, 1)) #처음 방문용 큐를 넣고 시작, depth정보 tuple로 저장
        while q:
            cur_node, cur_depth = q.popleft()
            max_depth = max(max_depth, cur_depth)
            if cur_node.left:
                q.append((cur_node.left, cur_depth + 1))
            if cur_node.right:
                q.append((cur_node.right, cur_depth + 1))
            
        return max_depth