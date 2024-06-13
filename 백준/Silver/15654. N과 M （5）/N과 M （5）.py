N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))

#N : 리스트 길이, M:수열 길이
def solution(N,M):
    ans = []
    def backtracking(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        for num in N_list:
            if num not in curr:
                curr.append(num)
                backtracking(curr)
                curr.pop()
    
    backtracking(curr=[])
    return ans

result = solution(N, M)
for ele in result:
    print(*ele)