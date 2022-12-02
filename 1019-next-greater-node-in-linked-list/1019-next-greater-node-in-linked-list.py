# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        if head is None:
            return []
        
        temp=head
        a=[]
        n=0
        while temp!=None:
            a.append(temp.val)
            temp=temp.next
            n+=1

        st=[]
        ans=[0]*n
        
        for i in range(n-1,-1,-1):
            while st and st[-1]<=a[i]:
                st.pop()
            if st:
                ans[i]=st[-1]
            else:
                ans[i]=0
                
            st.append(a[i])
            
        return ans
        