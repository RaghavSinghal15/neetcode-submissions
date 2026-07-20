# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root : return 
        inorder = []
        def dfs(root):
            nonlocal k
            if root and len(inorder)<k:
                dfs(root.left)
                if len(inorder)<k:
                    inorder.append(root.val)
                dfs(root.right)
            else: return 
        dfs(root)
        return inorder[-1]
