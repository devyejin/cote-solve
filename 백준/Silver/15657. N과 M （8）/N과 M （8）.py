N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

#비내림차순 수열
def solution(N,M):
    ans = []
    
    def backtracking(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for i in range(start, N):
            curr.append(nums[i])
            backtracking(i, curr)
            curr.pop()
    
    backtracking(start = 0, curr=[])
    return ans

result = solution(N,M)
for element in result:
    print(*element)
