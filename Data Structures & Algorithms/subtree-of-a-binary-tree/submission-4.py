# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def __init__(self):
        self.is_same = False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return 
        if root.val == subRoot.val:
            self.is_same = self.dfs(root, subRoot) or self.is_same
        
        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        
        return self.is_same

    def dfs(self, root, subRoot):

        if root == None and subRoot == None:
            return True
        if (root == None and subRoot != None) or (root != None and subRoot == None):
            return False
        if root.val != subRoot.val:
            return False

        is_same_left = self.dfs(root.left, subRoot.left)
        is_same_right = self.dfs(root.right, subRoot.right)

        return is_same_left and is_same_right



        

        
