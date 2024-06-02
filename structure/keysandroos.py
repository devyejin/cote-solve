class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [False] * len(rooms)  #방문 기록용
        
        # v에 연결되어 있는 모든 vertex에 방문, recursive로 구현
        def dfs(v):
            visited[v] = True
            for next_v in rooms[v]: 
                #무한루프 방지
                if visited[next_v] == False: #리스트 idx 접근은 O(1)
                    dfs(next_v)
            
        dfs(0)

        return all(visited) #all(iterable객체) : iterable 객체의 모든 요소가 True인지 확인 O(n)
        
        #디버깅용
        # return visited





#테스트용
instance = Solution()
rooms = [[1,3], [2,4], [0], [4], [], [3,4]]
print(instance.canVisitAllRooms(rooms))