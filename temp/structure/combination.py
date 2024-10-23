def solution(nums, k):
    result = []
    def backtracking(start, curr):
        if len(curr) == k:
            result.append(curr[:])
            return
        
        for i in range(start, len(nums)):
            curr.append(nums[i]) #현재값
            backtracking(i+1, curr) #다음값
            curr.pop()
    
    backtracking(start = 0, curr=[])    
    return result

    

print(solution(nums=[1,2,3,4], k=2))