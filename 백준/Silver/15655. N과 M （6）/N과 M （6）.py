N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))

#N : 리스트 길이, M:수열 길이
def solution(N,M):
    ans = []
    visited = {num : False for num in N_list} 
    
    def backtracking(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        for i in range(start, N):
            curr.append(N_list[i])
            backtracking(i+1, curr)
            curr.pop()

    backtracking(start = 0, curr=[])
    return ans

result = solution(N, M)
for ele in result:
    print(*ele)