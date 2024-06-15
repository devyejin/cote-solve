#1~N까지 자연수 중 중복 없이 M개를 고른 수열
#수열은 오름차순
N, M = map(int, input().split())

def solution(N,M):
    ans = []
    def backtracking(start, curr):
        if len(curr) == M:
            ans.append(curr[:])
            return

        for num in range(start, N+1):
            if num not in curr:
                curr.append(num)
                backtracking(num+1, curr)
                curr.pop()
                    
    backtracking(start = 1, curr = [])
    return ans

result = solution(N,M)
for ans in result:
    print(*ans)