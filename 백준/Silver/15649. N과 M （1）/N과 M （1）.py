N, M = map(int, input().split())

def solution(N,M):
    ans = []
    def backtracking(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return

        for num in range(1, N+1):
            if num not in curr:
                curr.append(num)
                backtracking(curr)
                curr.pop()
    
    backtracking([])
    return ans
    
result = solution(N, M)
for seq in result:
    print(*seq) 