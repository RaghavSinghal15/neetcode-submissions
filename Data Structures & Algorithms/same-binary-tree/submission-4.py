# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(curr1,curr2):
            if curr1 == None and curr2 == None: return True
            if curr1 and curr2:
                if curr1.val == curr2.val:
                    return dfs(curr1.right,curr2.right) and dfs(curr1.left,curr2.left)
            return False
        
        return dfs(p,q)