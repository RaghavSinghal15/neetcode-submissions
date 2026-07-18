# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def valid(self,node,low,high):
         
        if low < node.val < high:
            if node.right == None and node.left:
                return self.valid(node.left,low,node.val)
            elif node.left == None and node.right:
                return self.valid(node.right,node.val,high)
            elif node.left == None and node.right == None:
                return True
            else:
                return self.valid(node.right,node.val,high) and self.valid(node.left,low,node.val)
        else: return False 

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        return self.valid(root,float('-inf'),float('inf'))



        