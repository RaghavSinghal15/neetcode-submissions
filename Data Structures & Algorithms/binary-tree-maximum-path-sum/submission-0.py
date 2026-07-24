# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxsum = float("-inf")
        def dfs(root):
            nonlocal maxsum
            if root:
                left = dfs(root.left)
                right = dfs(root.right)
                maxsum = max(maxsum,root.val + left + right)
                return root.val + max(left,right) if root.val + max(left,right)>0 else 0
            else: return 0
        dfs(root)
        return maxsum