N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

#순열은 중복 OK, 결과집합은 중복 Nope -> Set

def solution(M):
    ans = set()
    def backtracking(start, curr):
        if len(curr) == M:
            ans.add(tuple(curr[:]))
            return
        
        for i in range(start, N):
            curr.append(nums[i])
            backtracking(i, curr)
            curr.pop()
    
    backtracking(start = 0, curr=[])
    return sorted(ans)

result = solution(M)
for ele in result:
    print(*ele)