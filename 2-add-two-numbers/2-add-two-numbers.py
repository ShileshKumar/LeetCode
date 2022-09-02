# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #create a dummy node which we will return as answer
        #create a temp pointer which is used for iteration
        temp=head=ListNode(0)
        carry=0
        #carry flag is set to 0 initially
        
        while l1!=None or l2!=None or carry>0:
            val1=val2=0
            if l1:
                val1=l1.val
            if l2:
                val2=l2.val
            sum1=val1+val2+carry
            carry=sum1//10
            temp.next=ListNode(sum1%10)
            temp=temp.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return head.next
        