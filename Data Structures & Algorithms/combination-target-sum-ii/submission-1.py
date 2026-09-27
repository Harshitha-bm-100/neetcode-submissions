class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        i = 0
        path = []
        output = []
        tot = 0

        def dfs(i, tot):
            if tot == target:
                output.append(path.copy())
                return 
            if i == len(candidates) or tot+candidates[i] > target:
                return


            path.append(candidates[i])
            tot+=candidates[i]

            dfs(i+1, tot)
            tot-=path.pop()
            while i+1<len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            dfs(i+1, tot)

          
        dfs(i, tot)
        return list(output)