# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, curr1: Optional[TreeNode], curr2: Optional[TreeNode]) -> bool:
            if curr1 is None and curr2 is None: return True
            if curr1 and curr2:
                if curr1.val == curr2.val:
                    return self.isSameTree(curr1.right,curr2.right) and self.isSameTree(curr1.left,curr2.left)
            return False   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if (root and subRoot) and root.val == subRoot.val:
            if self.isSameTree(root,subRoot):
                return True
        if not root: return False

        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)
