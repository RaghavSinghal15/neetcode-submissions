# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depth(self,node):
            if not node:
                return 0
            return max(1 + self.depth(node.left),1 + self.depth(node.right))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        leftdep = self.depth(root.left)
        rightdep = self.depth(root.right)
        diameter = max(leftdep+rightdep,self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right))
        return diameter
        
        
        