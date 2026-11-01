class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        alt = []
        for i in nums:
            if i not in alt:
                alt.append(i)

        nums[:len(alt)] = alt   
        return len(alt)
