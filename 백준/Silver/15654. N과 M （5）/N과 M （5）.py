N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))

#N : 리스트 길이, M:수열 길이
def solution(N,M):
    ans = []
    visited = {num : False for num in N_list} 
    
    def backtracking(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        for num in N_list:
            # if num not in curr: # O(n)
            if not visited[num]: #O(1) 으로 단축
                curr.append(num)
                visited[num] = True
                backtracking(curr)
                curr.pop()
                visited[num] = False
    
    backtracking(curr=[])
    return ans

result = solution(N, M)
for ele in result:
    print(*ele)