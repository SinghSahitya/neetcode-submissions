class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return nums

        m = len(nums) // 2
        L_array = nums[:m]
        R_array = nums[m:]

        L = self.sortArray(L_array)
        R = self.sortArray(R_array)
        l, r = 0, 0
        i= 0 
        sorted_array = [0] * n

        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                sorted_array[i]= L[l]
                l +=1
                i+=1
            else:
                sorted_array[i] = R[r]
                r+=1
                i+=1

        while l < len(L):
            sorted_array[i] = L[l]
            l+=1
            i+=1

        while r < len(R):
            sorted_array[i] = R[r]
            r+=1
            i+=1
        
        return sorted_array