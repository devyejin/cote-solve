class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number_of_islands = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)] 
        
        def bfs(x, y):
            q = deque()
            # 상하좌우
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            visited[x][y] = True # 방문 기록
            q.append((x, y))
            
            while q:
                cur_x, cur_y = q.popleft()
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]
                    if 0 <= next_x < m and 0 <= next_y < n:
                        if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                            visited[next_x][next_y] = True # 방문 기록
                            q.append((next_x, next_y)) # 방문할 곳 추가
        
        
        #recursive로 구현
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]: #미방문이라면
                    bfs(i,j)
                    number_of_islands += 1
        
        return number_of_islands