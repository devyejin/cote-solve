dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

N = int(input())
find_num = int(input())

r, c, d = 0, 0, 0
f_r, f_c = 0, 0

snail = [[0] * N for _ in range(N)]

# N^2 ~ 1까지 값 뿌리기
for num in range(N**2, 0, -1):
    #값 적용
    snail[r][c] = num

    #두번째 문제용
    if num == find_num:
        f_r, f_c = r + 1, c + 1

    #다음 좌표 찾기
    nr, nc = r + dr[d], c + dc[d]

    #맞는 방향인지 체크, 아니라면 방향 전환
    if nr < 0 or nr >= N or nc < 0 or nc >= N or snail[nr][nc] != 0:
        d = ( d + 1 ) % 4
        nr, nc = r + dr[d], c + dc[d]

    r, c = nr, nc

for ans in snail:
    print(*ans)

print(f_r, f_c)