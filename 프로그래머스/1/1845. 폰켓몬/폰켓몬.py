def solution(nums):
    answer = 0
    nums_set = set(nums)
    n = len(nums_set)
    if n > len(nums)/2:
        answer = len(nums)/2
    else:
        answer = n
    
    return answer