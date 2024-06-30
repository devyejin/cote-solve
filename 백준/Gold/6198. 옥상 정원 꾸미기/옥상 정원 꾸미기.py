import sys

N = int(sys.stdin.readline().strip())
height = [int(sys.stdin.readline().strip()) for _ in range(N)]

stack = []
temp_result = [N] * N
stack.append(0)

for i in range(1, N):
    while stack and height[stack[-1]] <= height[i]:
        temp_result[stack[-1]] = i
        stack.pop()
    stack.append(i)
    

result = [temp_result[i] - i -1 for i in range(N)]

print(sum(result))
