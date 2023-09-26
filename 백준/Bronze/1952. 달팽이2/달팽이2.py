M, N = map(int, input().split())

# 방향
# 우하좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
r, c, d, count = 0, 0, 0, 0

square = [[0] * N for _ in range(M)]
square[r][c] = 1

for _ in range(M*N):

    nr, nc = r + dr[d], c + dc[d]

    #방향 전환
    if nr >= M or nr < 0 or nc >= N or nc < 0 or square[nr][nc] == 1:
        d = (d+1) % 4
        count += 1

        nr, nc = r + dr[d], c + dc[d]

    r, c = nr, nc
    square[r][c] = 1
    
print(count-1) # 마지막엔 끝인데, 방향전환 발생해서 -1 보정