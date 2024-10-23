def twoSum(nums: list[int], target: int):
  nums.sort()
  l, r = 0, len(nums) - 1
  
  while l < r:
    sum = nums[l] + nums[r]
    if sum > target:
      r -= 1
    elif sum < target:
      l += 1
    elif sum == target:
      return [nums[l], nums[r]]

print(twoSum([2,7,11,15], 9))