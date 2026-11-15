class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            while l<r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
        return res

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue

            res_3 = self.threeSum(nums[i+1:], target-a)
            for i in res_3:
                res.append([a]+i)

        return res

