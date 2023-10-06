from collections import deque

N, M = map(int, input().split()) #도착 지점

graph = []

for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(r,c): #시작 지점
    #     상  하 좌  우
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)

    #자료 구조
    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0  or nc >= M:
                continue

            if graph[nr][nc] == 0: #벽인 경우
                continue

            if graph[nr][nc] == 1:
                graph[nr][nc] = graph[r][c] + 1 #길이 카운트
                queue.append((nr,nc)) #좌표 추가


    return graph[N-1][M-1]

print(bfs(0,0))