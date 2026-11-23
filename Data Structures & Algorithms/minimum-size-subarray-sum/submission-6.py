class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        window = []
        res = 10 ** 5 + 1
        win_sum = 0
        while r < len(nums):
            if win_sum < target:
                win_sum += nums[r]
                print('cur sum', win_sum)
                
            while win_sum >= target:
                res = min(res, len(nums[l:r+1]))  
                print('res',res, win_sum , l)          
                win_sum -= nums[l]
                l += 1
            r += 1

        if res > len(nums):
            return 0
        return res