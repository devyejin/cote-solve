from collections import deque

#테스트용
graph = {
      "A" : ["B", "D", "E"]
    , "B" : ["A", "C", "D"]
    , "C" : ["B"]
    , "D" : ["A", "B" ]
    , "E" : ["A"]
}
class Solution:

    def numIslands(self, grid: list[list[str]]) -> int:
        number_of_islands = 0 # bfs 돌 때 마다 +1
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)] #방문 기록용
        
        def bfs(x,y):
            q = deque()
            #상하좌우
            dx = [1, -1, 0, 0]
            dy = [0, 0, 1, -1]
            visited[x][y] = True #방문 기록
            q.append((x,y)) 
            
            while q:
                cur_x , cur_y = q.popleft()
                # visited[cur_x][cur_y] = True #방문 기록
                #4가지 방향에 대해 갈 수 있는 곳 확인
                for i in range(4):
                    next_x = cur_x + dx[i]
                    next_y = cur_y + dy[i]
                    if 0 <= next_x < m and 0 <= next_y < n:
                        if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                            # visited[next_x][next_y] = True #방문! <-- 위쪽에서 pop할때 방문 체크하는게 맞는거같음
                            # 아님! 어차피 FIFO니까,Queue에 추가할 때 방문기록을 남기는게 중복 방지됨!
                            visited[next_x][next_y] = True
                            q.append((next_x, next_y)) #방문할 곳 추가
        
        
        #recursive로 구현
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]: #미방문이라면
                    bfs(i,j)
                    number_of_islands += 1
        
        return number_of_islands

instance = Solution()
print(instance.numIslands(graph))   

#bfs를 밖에 선언하면 m,n,grid,visited 를 다 매개변수로 넘겨줘야함
#bfs는 한 번만 호출하니까 할 만 한데, dfs의 경우 여러번 호출해야하니 
#밖에 선언하면 번잡스러움 내부에 선언!