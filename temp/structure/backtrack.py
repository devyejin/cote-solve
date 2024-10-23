def permute(nums):
    
    def backtrack(curr):
        #종료 조건
        if len(curr) == len(nums):
            ans.append(curr[:])
            return
        
        for num in nums:
            if num not in curr:
                curr.append(num)
                backtrack(curr)
                curr.pop()
    
    ans = [] #가능한 순열들
    backtrack([])
    return ans

print(permute([1,2,3]))