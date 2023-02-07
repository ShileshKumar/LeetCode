# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d={}
        temp=head
        while temp:
            if temp.val in d:
                d[temp.val]+=1
            else:
                d[temp.val]=1
            temp=temp.next
        #print(d)
        res=curr=ListNode()
        
        for k,v in d.items():
            if v==1:
                curr.next=ListNode(k)
                curr=curr.next
        return res.next