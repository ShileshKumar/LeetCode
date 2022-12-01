# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=head
        l=[]
        if head is None:
            return head
        while a is not None:
            l.append(a.val)
            a=a.next
        s=[0]*len(l)
        s[-1]=l[-1]
        for i in range(len(l)-2,-1,-1):
            s[i]=max(s[i+1],l[i])
        ans=[]
        for i in range(len(l)):
            if l[i]==s[i]:
                ans.append(l[i])
        h=ListNode(ans[0])
        n=h
        for i in range(1,len(ans)):
            new=ListNode(ans[i])
            n.next=new
            n=n.next
        return h