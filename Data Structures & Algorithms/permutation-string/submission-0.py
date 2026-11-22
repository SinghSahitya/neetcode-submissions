class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_c = Counter(s1)
        l = 0
        r = len(s1) - 1
        flag = False
        while r < len(s2):
            if Counter(s2[l:r+1]) == s1_c:
                flag = True
                break
            
            r += 1
            l+=1
        return flag