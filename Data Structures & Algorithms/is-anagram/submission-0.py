class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for i in range(len(s)):
            my_dict[s[i]] = my_dict.get(s[i], 0) + 1

        for j in range(len(t)):
            if t[j] in my_dict:
                my_dict[t[j]] -= 1
                if my_dict[t[j]] == 0:
                    del my_dict[t[j]]
            else:
                return False
        
        if not my_dict:
            return True
        return False
