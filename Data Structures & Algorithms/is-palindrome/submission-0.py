class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = [str.lower(char) for char in s if char.isalnum()]
        print(char_list)
        i = 0
        j = len(char_list)-1

        while i<j:
            if char_list[i] != char_list[j]:
                return False
            i += 1
            j -= 1

        return True
