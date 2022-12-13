# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n=0
        start=node=head
        while start:
            n+=1
            start=start.next
        m=n//2
        counter=0
        while node:
            if counter==m:
                return node
            else:
                node=node.next
                counter+=1
        return None
        
        