class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = {}
        max_len = 0
        max_rep = 0
        i = 0
        for j in range(len(s)):
            if s[j] not in my_dict:
                my_dict[s[j]] = 0
            my_dict[s[j]]+=1
            max_rep = max(max_rep, my_dict[s[j]])

            while max_rep + k < (j-i+1):
                my_dict[s[i]]-=1
                max_rep = max(my_dict.values())
                i+=1
            max_len = max(max_len, j-i+1)

        return max_len