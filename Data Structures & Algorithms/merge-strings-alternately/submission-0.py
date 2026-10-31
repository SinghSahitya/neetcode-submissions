class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        chose = True
        if len(word1) > len(word2):
            length = len(word2)
        else:
            length = len(word1)
            chose = False
        ans = ''
        for i in range(length):
            ans += word1[i] + word2[i]

        if chose == True:
            return ans + word1[length:]
        return ans + word2[length:]