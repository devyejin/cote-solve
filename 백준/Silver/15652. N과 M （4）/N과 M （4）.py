N, M = map(int, input().split())

def solution(N,M):
    ans = []
    def backtracking(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(start, N+1):
            curr.append(i)
            backtracking(i, curr) #현재값 부터 넣으니까
            curr.pop()
    
    backtracking(start = 1, curr = [])
    return ans


result = solution(N,M)
for element in result:
    print(*element)