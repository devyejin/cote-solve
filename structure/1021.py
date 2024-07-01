import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
location = list(map(int, input().split()))
dq = deque([i for i in range(1, N+1)])

count = 0
for i in location:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            # <- 왼쪽 방향으로 이동하는게 이동횟수가 더 적게드는 경우
            if dq.index(i) < len(dq) / 2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    count += 1
            else: # -> 방향이 이동횟수가 더 적은 경우
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    count += 1

print(count)