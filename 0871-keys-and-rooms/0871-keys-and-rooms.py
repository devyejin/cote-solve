class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [] #방문 기록용
        
        # v에 연결되어 있는 모든 vertex에 방문, recursive로 구현
        def dfs(v):
            visited.append(v)
            for next_v in rooms[v]:
                #무한루프 방지
                if next_v not in visited:
                    dfs(next_v)
            
        dfs(0)
        if len(visited) == len(rooms):
            return True
        else:
            return False