import sys


stack = []

K = int(input())
for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))


import sys


stack = []

K = int(input())
for _ in range(K):
    num = int(sys.stdin.readline())
    if num:
        stack.append(num)
    else: # 0은 False 평가
        stack.pop()
print(sum(stack))

    
