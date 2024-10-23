class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      table = {}
      for i, num in enumerate(nums):
        diff = target - num
        if diff in table:
          return [i, table[diff]]
        else:
          table[num] = i

