class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rotate = k % len(nums)

        if rotate > 0:
            to_shift = nums[len(nums)-rotate:]
            nums[:rotate], nums[rotate:] =  to_shift, nums[:len(nums)-rotate]