import sys
from collections import deque, defaultdict

#인접행렬 -> 인접리스트(딕셔너리)
input = sys.stdin.readline

V, E = map(int, input().split())

adj_list = defaultdict(list) #기본값이 빈 리스트인 딕셔너리 생성

for _ in range(E):
    start, end = map(int, input().split())
    adj_list[start].append(end) # key가 start인 value에 end값 넣어줌
    adj_list[end].append(start)

# print(adj_list)

def bfs(root_v):
    Q = deque()
    Q.append(root_v) #처음 방문 vertex 넣고 시작
    visited = [] #방문 기록용
    visited_check = set() #방문 확인용
    
    while Q:
        current = Q.popleft()
        if current not in visited_check:
            visited.append(current) #방문
            visited_check.add(current) #방문 체크
            for destination in adj_list[current]:
                if destination not in visited_check:
                    Q.append(destination)
    
    return visited
            
print(bfs(1))