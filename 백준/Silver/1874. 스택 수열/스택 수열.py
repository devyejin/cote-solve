N = int(input())
seq = [int(input()) for _ in range(N)]
stack = []
result = []
idx = 0

#수열 길이만큼 idx로 돌면서
for i in range(1, N+1):
    stack.append(i)
    result.append('+')
    
    while stack and stack[-1] == seq[idx]:
        stack.pop()
        result.append('-')
        idx += 1
    
if stack:
    print('NO')
else:
    for ele in result:
        print(ele)