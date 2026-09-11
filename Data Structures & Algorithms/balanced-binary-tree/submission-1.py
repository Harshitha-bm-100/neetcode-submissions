# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root == None:
                return True, 0
            left_balanced, left = dfs(root.left)
            right_balanced, right = dfs(root.right)

            current_balanced = (left_balanced and right_balanced and abs(left-right)<=1)
            return current_balanced, max(left, right)+1
            

        balanced, height = dfs(root)
        return balanced
        