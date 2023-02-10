# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self,root):
        if root==None:
            return 0
        
        left=self.helper(root.left)
        if left==-1:
            return -1
        
        right=self.helper(root.right)
        if right==-1:
            return -1
        
        if abs(left-right)>1:
            return -1
        
        return 1+max(left,right)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)!=-1