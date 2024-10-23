from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        shortest_path_len = -1 # 도착할 수 없는 경우 -1 반환
        row, col = len(grid), len(grid[0])
        
        if grid[0][0] == 1 or grid[row-1][col-1] == 1:
            return shortest_path_len #시작점 or 도착지가 못 가는 곳이라면 조기return
        
        visited = [[False] * col for _ in range(row)]
        queue = deque()
        queue.append((0,0,1)) #시적점 넣기, 길이 정보 추가
        visited[0][0] = True #방문 표시
        
        delta = [(-1,0), (1,0), (0,-1), (0,1)
                 ,(-1,-1), (-1,1), (1,1), (1,-1)]
        
        while queue:
            
            cur_r, cur_c, cur_len = queue.popleft()
            
            #목적지라면 반환
            if cur_r == row - 1 and cur_c == col - 1:
                shortest_path_len = cur_len
                return shortest_path_len #전체 순회 하지 않고 반환
            
            #방문할 수 있는 곳 확인
            for dr, dc in delta:
                next_r = cur_r + dr
                next_c = cur_c + dc
                if 0 <= next_r < row and 0 <= next_c < col:
                    if grid[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        queue.append((next_r, next_c, cur_len + 1)) #방문 예약
                        visited[next_r][next_c] = True #방문 표시
        
        return shortest_path_len