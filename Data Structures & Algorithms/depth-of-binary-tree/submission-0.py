# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 0


        def depth(node,height):
            nonlocal maxdepth
            if node is None:
                maxdepth = max(maxdepth,height)
                return
            else:
                height+=1
                depth(node.left,height)
                depth(node.right,height)

        depth(root,0)

        return maxdepth