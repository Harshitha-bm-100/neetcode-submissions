class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(s.split()).lower()
        my_s = ""
        for i in range(len(s)):
            if s[i].isalnum() == True:
                my_s += s[i]

        i = 0
        j = len(my_s) - 1

        while i<=j:
            if my_s[i] != my_s[j]:
                return False
            i += 1
            j -= 1
        return True


