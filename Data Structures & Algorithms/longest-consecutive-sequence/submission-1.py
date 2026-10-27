class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        arr = sorted(nums)
        i = 0
        max_len = 1
        ans = 1
        while i < len(nums) - 1:
            if arr[i+1] - arr[i] == 1:
                ans += 1            
            elif arr[i+1] - arr[i] > 1:
                ans = 1
            if max_len < ans:
                max_len = ans
            i += 1    
        return max_len