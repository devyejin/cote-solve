N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

#순열은 중복 OK, 결과집합은 중복 Nope -> Set

def solution(M):
    ans = set()
    def backtracking(curr):
        if len(curr) == M:
            ans.add(tuple(curr[:]))
            return
        
        for num in nums:
            curr.append(num)
            backtracking(curr)
            curr.pop()
    
    backtracking(curr=[])
    return sorted(ans)

result = solution(M)
for ele in result:
    print(*ele)