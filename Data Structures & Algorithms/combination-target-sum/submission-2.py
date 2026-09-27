class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        i = 0
        path = []
        output = []
        tot = 0
        def dfs(i, tot):
            #base case
            if tot == target:
                output.append(path.copy())
                return
            if tot>target or i == len(nums):
                return 

            path.append(nums[i])
            tot+=nums[i]

            dfs(i , tot)
            tot -= path.pop()
            dfs(i+1, tot)
            
        
        dfs(i, tot)
        return output