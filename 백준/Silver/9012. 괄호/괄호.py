import sys

input = sys.stdin.readline

from collections import deque

n = int(input())
for _ in range(n):
    parentheses = input().rstrip() # 우변 공백 제거

    stack = deque()

    for parenthese in parentheses:
        if parenthese == '(':
            stack.append(parenthese)

        elif stack:
            stack.pop()

        else: # stack이 비었다면
            stack = True
            break

    print("YES" if not stack else "NO")

