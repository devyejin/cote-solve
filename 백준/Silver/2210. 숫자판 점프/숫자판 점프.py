import sys

input = sys.stdin.readline

from collections import deque

#    상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(r, c, num):  # (좌표, 현재값)

    stack = deque([(r, c, num)]) #튜플 형태로 값 묶어서 stack에 저장

    while stack:
        r, c, num = stack.pop()

        # 종료 조건
        if len(num) == 6:
            cases.add(num)
            continue

        # 자기 자리에서 4방향으로 5번 이동
        for dir in range(4):
            nr, nc = r + dr[dir], c + dc[dir]
            if 0 <= nr < 5 and 0 <= nc < 5:
                stack.append((nr, nc, num + str(matrix[nr][nc])))


matrix = [list(map(int, input().split())) for _ in range(5)]

cases = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, str(matrix[i][j])) # (현재위치 좌표, 현재값(문자로처리))

print(len(cases))
