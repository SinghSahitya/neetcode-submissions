class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        occur = Counter(nums)
        
        for k , v in occur.items():
            if v > (n/2):
                return k