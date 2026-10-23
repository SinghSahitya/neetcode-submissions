class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        occur = Counter(nums)
        
        for i in nums:
            if occur[i] > (n/2):
                return i