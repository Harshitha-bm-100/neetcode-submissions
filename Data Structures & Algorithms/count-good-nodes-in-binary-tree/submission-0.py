# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        greatest = root.val
        def dfs(root, greatest):
            count = 0
            if root == None:
                return 0
            if root.val >= greatest:
                greatest = root.val
                count = 1
            return count+dfs(root.left, greatest)+dfs(root.right, greatest)

        return dfs(root, greatest)


