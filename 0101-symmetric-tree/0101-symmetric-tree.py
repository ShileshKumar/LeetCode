# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            que=[root]
            lev=[0]
            a={}
            while len(que)>0:
                x=que.pop(0)
                y=lev.pop(0)
                if y not in a:
                    if x!=None:
                        a[y]=[x.val]
                    else:
                        a[y]=['N']
                else:
                    if x!=None:
                        a[y].append(x.val)
                    else:
                        a[y].append('N')
                if x:
                    if x.left:
                        que.append(x.left)
                        lev.append(y+1)
                    else:
                        que.append(None)
                        lev.append(y+1)
                        
                    if x.right:
                        que.append(x.right)
                        lev.append(y+1)
                    else:
                        que.append(None)
                        lev.append(y+1)
            for i in a:
                if a[i]!=a[i][::-1]:
                    return False
        return True
            
                    
                    
                    
                        