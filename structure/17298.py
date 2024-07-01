import sys


N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))

result = [-1 for _ in range(N)] #1보다 큰 정수니까 -1로 초기화
stack = []
stack.append(0)

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        # A[stack[-1]] <  A[i] 라면 i는 idx=stack[-1]의 오큰수
        #idx= stack[-1] 의 오큰수는 정해졌으니까 stack에서 pop
        result[stack.pop()] = A[i]
    stack.append(i)
            
print(*result)