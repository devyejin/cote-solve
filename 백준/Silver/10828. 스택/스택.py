# pop : 빼고
# empty 비었으면 1,  아니면 0
# top 가장 위에 있는 정수, 없으면 -1

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque()

for _ in range(n):
    command = input().rstrip()

    if " " in command: #push인 경우에만 공백이 있음
       num = int(command.split()[1])
       stack.append(num)

    elif command == 'top':
        if stack:
            print(stack[-1]) # 제일 오른쪽 숫자 (pop()은 idx=0나옴)
        else:
            print(-1) #stack비었으면 -1 출력
        
        
    elif command == 'size':
        print(len(stack))
    
    elif command == 'empty':
        if stack: # stack이 안 빈 경우
            print(0)
        else:
            print(1)
    
    elif command == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1) # 스택이 비었으면 -1 출력
        


