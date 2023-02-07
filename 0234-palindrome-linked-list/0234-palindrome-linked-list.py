# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #step 1: creating a temp node for clone our linkedlist
        curr=head
        temp=ListNode(0)
        dummy=temp #dummy pointer points to the temp node
        #copying each value from curr node to temp node
        while curr:
            dummy.next=ListNode(curr.val) 
            curr=curr.next
            dummy=dummy.next
        #now the head1 become the head pointer for temp dummy node
        head1=temp.next #as temp stores 0, temp.next stores the cloned head
        
        #step 2: we now reverse the cloned temp.next
        prev=None
        curr1=head1
        while curr1:
            nxt=curr1.next
            curr1.next=prev
            prev=curr1
            curr1=nxt
        #prev stores the reversed head, so re-assign it to head1
        head1=prev
        
        #step 3: Now compare the values of the dummy temp reversed node and the original curr head node given
        #print(head)
        #print(head1)
        while head!=None and head1!=None:
            #If they are equal check for every node
            if head.val==head1.val:
                head=head.next
                head1=head1.next
            else:
                return False
        return True