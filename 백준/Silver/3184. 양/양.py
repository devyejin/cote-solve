'''
 조금이라도 더 빨리 발견할 여지 없이 완탐해야하니까
 bfs 아닌 dfs로 택!
 연결상태 자료구조는 matrix가 적합해보임

 연속된 #이 아닌 요소를 찾은다음 => 그 구역내에서 num(v) num(o) 구해서 비교
 둘 중 큰 갯수만 카운팅

 이걸 반복해서 카운팅 누적 후 출력
'''

# 자료구조 입력 받기
R, C = map(int, input().split())
MAP = [[0] * C for _ in range(R)]

for i in range(R):
    line = input().strip()
    MAP[i] = list(line)

# 4방 탐색하며 #이 아닌 무리에서 v랑 o 갯수 카운팅-> map 변형해도 되니까 돌면 # 으로 바꿔버리기
# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(r, c):
    cnt_v, cnt_o = 0, 0
    stack = [(r, c)]

    while stack:
        r, c = stack.pop()

        if MAP[r][c] == 'v':
            cnt_v += 1
        if MAP[r][c] == 'o':
            cnt_o += 1
        MAP[r][c] = '#' #방문처리(울타리로 만들어버리기)


        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            # if nr < 0 or nr >= R or nc < 0 or nc >= C or MAP[nr][nc] == '#':
            #     continue
            # stack.append((nr, nc))
            if 0 <= nr < R and 0 <= nc < C and MAP[nr][nc] != '#':
                stack.append((nr,nc))

    return cnt_v, cnt_o

v, o = 0, 0
for r in range(R):
    for c in range(C):
        if MAP[r][c] != '#':
            cnt_v, cnt_o = dfs(r, c)

            if cnt_v >= cnt_o:
                cnt_o = 0
            else:
                cnt_v = 0

            v += cnt_v
            o += cnt_o

print(o, v)


