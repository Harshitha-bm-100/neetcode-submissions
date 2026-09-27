class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        i = 0
        path = []
        output = []

        def dfs(i):
            #base case
            if i == len(nums):
                output.append(path.copy())
                return 
            
            path.append(nums[i])
            dfs(i+1)
            path.pop()

            dfs(i+1)

        dfs(i)
        return output