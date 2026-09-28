class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        path = []
        output = []

        def dfs(i):
            #base case
            if i==len(nums):
                output.append(path.copy())
                return
            
            #include
            path.append(nums[i])
            dfs(i+1)
            path.pop()

            #skip
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
        
        dfs(0)
        return output

