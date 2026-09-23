class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            y = nums.index(x, i + 1) if x in nums[i + 1:] else -1
            if y != -1 and y != i:
                return [i, y]