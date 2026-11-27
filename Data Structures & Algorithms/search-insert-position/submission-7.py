class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid  # Target found, return index
            elif nums[mid] < target:
                low = mid + 1  # Search the right half
            else:
                high = mid - 1  # Search the left half

        if nums[mid] > target:
            return mid 
        else:
            return mid + 1