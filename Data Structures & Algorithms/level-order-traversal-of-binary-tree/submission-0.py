# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        i = 0

        def dfs(root, i):
            if root == None:
                return
            if len(output)<i+1:
                output.append([])
            dfs(root.left, i+1)
            dfs(root.right, i+1)

            output[i].append(root.val)
        
        dfs(root, i)
        return output


