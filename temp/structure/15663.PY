N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()  # 중복된 수열을 방지하기 위해 정렬

def solution(N, M):
    tmp_ans = set()
    visited = [False] * N  # 방문 여부를 체크하는 리스트

    def backtracking(curr):
        if len(curr) == M:
            tmp_ans.add(tuple(curr[:]))  # 리스트 -> 튜플로 변환 후, set에 추가
            return
        
        for i in range(N):
            if not visited[i]:
                curr.append(nums[i])
                visited[i] = True
                backtracking(curr)
                curr.pop()
                visited[i] = False

    backtracking(curr=[])  
    return sorted(list(tmp_ans))

result = solution(N, M)
for ele in result:
    print(*ele)