import sys
from collections import deque

N = int(input())
tops = list(map(int, sys.stdin.readline().split()))

stack = []
result = [0] * N

for i in range(N):
    while stack and tops[stack[-1]] <= tops[i]:
        stack.pop()
    #크다면
    if stack:
        result[i] = stack[-1] + 1
    stack.append(i) 

print(*result)