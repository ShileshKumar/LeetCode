# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root,sum):
            if root==None:
                return 0
            if root.left==None and root.right==None:
                sum=sum*2+root.val
                return sum
            return (dfs(root.left,2*sum+root.val)+dfs(root.right,2*sum+root.val))
        if root==None:
            return 0
        return dfs(root,0)
    