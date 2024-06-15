#N개의 자연수 중 M 개를 고른 수열, 중복 수열X
N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def soultion(N,M):
    ans = set() 
    visited = [False] * N
    def backtracking(start, curr):
        if len(curr) == M:
            # ans.add(curr[:])
            ans.add(tuple(curr[:]))
            return
        
        for i in range(start, N):
            if not  visited[i]:
                curr.append(nums[i])
                visited[i] = True
                backtracking(i+1, curr)
                curr.pop()
                visited[i] = False
    backtracking(start= 0, curr=[])
    return sorted(ans)

result = soultion(N,M)
for ele in result:
    print(*ele)