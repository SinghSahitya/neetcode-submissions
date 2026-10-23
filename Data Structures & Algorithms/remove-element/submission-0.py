class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        occur = Counter(nums)
        length = len(nums)

        for j in range(occur[val]):
            nums.remove(val)

  
        return length - occur[val]