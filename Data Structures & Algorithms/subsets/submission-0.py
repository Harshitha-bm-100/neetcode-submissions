class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        path = []
        i = 0
        
        def dfs(i):
            output.append(path.copy())
                
            for j in range(i, len(nums)):
                path.append(nums[j])
                dfs(j+1)
                path.pop()

        dfs(i)
        return output