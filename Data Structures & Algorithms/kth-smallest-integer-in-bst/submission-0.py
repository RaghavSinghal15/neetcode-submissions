# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root : return 
        stack = []
        def dfs(root):
            nonlocal k
            if root and len(stack)<k:
                dfs(root.left)
                if len(stack)<k:
                    stack.append(root.val)
                dfs(root.right)
            else: return 
        dfs(root)
        return stack[-1]
