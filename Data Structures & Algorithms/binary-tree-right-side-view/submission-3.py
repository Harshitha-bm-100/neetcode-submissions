# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []
        i = 0
        if root == None:
            return levels
        def dfs(root, i):
            if root == None:
                return 
            if i > len(levels)-1:
                levels.append([])
            dfs(root.left, i+1)
            dfs(root.right, i+1)
            levels[i].append(root.val)
            

        dfs(root, i)
        res = []
        for level in levels:
            res.append(level[-1])
        return res
