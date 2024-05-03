import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

m, n, k = map(int, input().split())
arr = [[0] * m for _ in range(n)]

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):   
        for j in range(y1, y2): 
            arr[i][j] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    arr[x][y] = 1 
    cnt = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
            cnt += dfs(nx, ny) 
    return cnt

answer = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            answer.append(dfs(i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i, end=" ")