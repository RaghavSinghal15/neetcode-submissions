# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if root is None: return 0
            leftdep = dfs(root.left)
            rightdep = dfs(root.right)
            res = max(leftdep+rightdep,res)
            return 1 + max(leftdep,rightdep)
        dfs(root)
        return res
        
        