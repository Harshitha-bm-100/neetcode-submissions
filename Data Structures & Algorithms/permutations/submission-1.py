class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False]*len(nums)
        path = []
        output = []
        def dfs(i):
            if len(path)==len(nums):
                output.append(path.copy())
                return
            for j in range(len(nums)):
                if visited[j]:
                    continue
                path.append(nums[j])
                visited[j]=True

                dfs(j)

                path.pop()
                visited[j]=False
        dfs(0)
        return output