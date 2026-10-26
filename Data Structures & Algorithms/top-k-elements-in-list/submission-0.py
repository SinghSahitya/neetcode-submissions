class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ans_list = [item[0] for item in freq.most_common(k)]
        return ans_list
        