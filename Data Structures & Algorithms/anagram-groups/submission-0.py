class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        output = []

        i=0
        for s in strs:
            key = tuple(sorted(s))
            if key not in my_dict:
                my_dict[key] = i
                output.append([s])
                i+=1
            else:
                output[my_dict[key]].append(s)
        return output