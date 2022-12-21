# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        #base condition to check whether the head is NULL/not
        if head==None:
            return head
        #take a dummy node
        dummy=ListNode(0)
        #assign head to next of the dummy node
        dummy.next=head
        curr=dummy
        while curr.next!=None:
            #if the next of curr's val==val given
            if curr.next.val==val:
                #skip that node
                curr.next=curr.next.next
            else:
                #iterate further
                curr=curr.next
        #return dummy.next which is the resultant head node
        return dummy.next