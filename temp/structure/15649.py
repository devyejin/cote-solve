# 1~ N까지의 자연수
# 중복 없이 M개를 고른 수열
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
    
# * : 언패킹 연산자 seq = [1, 2, 3] -> *seq 하면 1 2 3 