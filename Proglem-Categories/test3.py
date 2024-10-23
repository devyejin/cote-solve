class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      for i in range(len(nums)):
        #필요한 값
        diff = target - nums[i]
        
        #diff가 존재 한다면
        if diff in nums:
          return [[i, ]]
solution = Solution()
print(solution.twoSum(nums = [2,7,11,15], target = 9))