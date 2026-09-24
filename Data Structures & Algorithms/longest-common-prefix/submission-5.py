class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        j = 0
        shortest_length = len(strs[0])
        for i in range(shortest_length):
            for j in strs[1:]:
                try:
                    if j[i] != strs[0][i]:
                        return ans
                except:
                    return ans
            ans += strs[0][i]
        return ans