class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []
        i = 0
        
        def dfs(i):
            if i == len(nums):
                output.append(path.copy())
                return 
            path.append(nums[i])
            dfs(i+1)
            path.pop()
        
            dfs(i+1)

        dfs(i)
        return output