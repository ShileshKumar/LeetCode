# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,l1,l2):
        head1=ListNode(0)
        curr=head1
        while l1 and l2:
            if l1.val<l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        if l1:
            curr.next=l1
        if l2:
            curr.next=l2
        return head1.next
        
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        head=self.merge(lists[0],lists[1])
        for i in range(2,len(lists)):
            head=self.merge(head,lists[i])
        return head