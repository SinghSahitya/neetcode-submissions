from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t or len(t) > len(s):
            return ""

        check = Counter(t)
        required = len(check)
        formed = 0

        l = 0
        min_length = float('inf')
        res = ""

        for r in range(len(s)):

            char = s[r]

            if char in check:
                check[char] -= 1

                if check[char] == 0:
                    formed += 1

            while formed == required:

                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    res = s[l:r+1]

                char = s[l]

                if char in check:
                    check[char] += 1

                    if check[char] > 0:
                        formed -= 1

                l += 1

        return res