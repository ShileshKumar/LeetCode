# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp=head
        n=0
        ll=[]
        while temp!=None:
            ll.append(temp.val)
            n+=1
            temp=temp.next
            
        maxTwinSum=-1
        for i in range((n//2)):
            twinSum=ll[i]+ll[n-i-1]
            maxTwinSum=max(maxTwinSum,twinSum)
            
        return maxTwinSum