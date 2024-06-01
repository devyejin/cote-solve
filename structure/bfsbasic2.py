import sys
from collections import deque

#인접 행렬로 구현
input = sys.stdin.readline

V, E = map(int,input().split()) 

adj_matrix = [[0] * (V+1) for _ in range(V+1)]

for _ in range(E):
    start, end = map(int, input().split())
    adj_matrix[start][end] = 1
    adj_matrix[end][start] = 1

def bfs(root_v):
    Q = deque()
    Q.append(root_v) #처음 방문 vertex 넣고 시작
    visited = [] #방문 기록용
    
    while Q:
        current = Q.popleft()
        if current not in visited:
            visited.append(current) #방문
        for destination in range(V+1): #현재 노드가 방문할 수 있는 곳 -> Queue에 넣기
            if adj_matrix[current][destination] == 1 and destination not in visited:
                Q.append(destination)
    
    return visited
            
print(bfs(1))