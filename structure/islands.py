from collections import deque

graph = {
      "A" : ["B", "D", "E"]
    , "B" : ["A", "C", "D"]
    , "C" : ["B"]
    , "D" : ["A", "B" ]
    , "E" : ["A"]
}

def numIslands(self, grid: List[List[str]]) -> int:
    number_of_islands = 0
    m = len(grid)
    n = len(grid[0])
    visited = [[False] * n for _ in range(m)] #방문 기록용
    
    def bfs(x,y):
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        visited[x][y] = True
        queue = deque((x,y))
        while queue:
            cur_x, cur_y = queue.popleft()
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                # if 방문하면 안되는 좌표
                if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
                    if grid[next_x][next_y] == "1" and not visited[next_x][next_y]:
                        visited[next_x][next_y] = True
                        queue.append((next_x, next_y))
    
    for i in range(m):
        for j in range(n):
            #if 땅이면서 & 방문 안했을 때
            if grid[i][j] == "1" and not visited[i][j]: 
                bfs(i, j)
                number_of_islands += 1 # bfs를 돌 때마다 카운트
    
    return number_of_islands


#bfs를 밖에 선언하면 m,n,grid,visited 를 다 매개변수로 넘겨줘야함
#bfs는 한 번만 호출하니까 할 만 한데, dfs의 경우 여러번 호출해야하니 
#밖에 선언하면 번잡스러움 내부에 선언!