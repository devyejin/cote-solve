N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

#추가 하는 경우, 안하는 경우 2가지의 dfs 가 동작
def dfs(idx, sum):
    global count
    
    if idx >= N:
        return
    
    #종료 조건
    if sum + nums[idx] == S:
        count += 1
    
    dfs(idx + 1, sum) # 추가 안하는 경우
    dfs(idx + 1, sum + nums[idx]) #추가하는 경우
    
    return count


result = dfs(idx=0, sum=0)
print(result)