import sys
from collections import deque

N = int(sys.stdin.readline().strip())
dq = deque()

result = []

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    key = command[0]
    if key == 'push_front':
        value = command[1]
        dq.appendleft(value)
    elif key == 'push_back':
        value = command[1]
        dq.append(value)
    elif key == 'pop_front':
        if dq:
            result.append(dq.popleft())
        else:
            result.append(-1)
    elif key == 'pop_back':
        if dq:
            result.append(dq.pop())
        else:
            result.append(-1)
    elif key == 'size':
        result.append(len(dq))
    elif key == 'empty':
        if dq:
            result.append(0)
        else:
            result.append(1)
    elif key == 'front':
        if dq:
            result.append(dq[0])
        else:
            result.append(-1)
    elif key == 'back':
        if dq:
            result.append(dq[-1])
        else:
            result.append(-1)

for ele in result:
    print(ele)