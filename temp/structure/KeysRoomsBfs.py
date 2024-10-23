from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [False] * len(rooms)  #방문 기록용
        
        # v에 연결되어 있는 모든 vertex에 방문, recursive로 구현
        def bfs(v):
            queue = deque()
            queue.append(v) #방문예약
            visited[v] = True #방문 기록

            while queue:
                cur_v = queue.popleft()
                for next_v in rooms[cur_v]:
                    if visited[next_v] == False:
                        queue.append(next_v) #방문예약
                        visited[next_v] = True #방문 기록
            
        dfs(0)

        return all(visited) #all(iterable객체) : iterable 객체의 모든 요소가 True인지 확인 O(n)
        
        #디버깅용
        # return visited





#테스트용
instance = Solution()
rooms = [[1,3], [2,4], [0], [4], [], [3,4]]
print(instance.canVisitAllRooms(rooms))