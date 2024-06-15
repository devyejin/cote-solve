N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))

def solution(N,M):
    ans = []
    
    def backtracking(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        
        for num in N_list:
            #들어있어도 그냥 순차적으로 순회
            curr.append(num)
            backtracking(curr)
            curr.pop()
        
    backtracking(curr=[])
    return ans

result = solution(N,M)
for ele in result:
    print(*ele)