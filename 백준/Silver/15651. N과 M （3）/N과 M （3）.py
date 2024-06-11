#1~N까지의 자연수
#N개를 고른 수열
#같은 수 골라도 됨 
N, M = map(int, input().split())

def solution(N,M):
    ans = []
    def backtracking(curr):
        if len(curr) == M:
            ans.append(curr[:])
            return
        for num in range(1, N+1):
            curr.append(num)
            backtracking(curr)
            curr.pop()
        
    backtracking(curr=[])
    return ans

result = solution(N,M)
for element in result:
    print(*element)