class Solution:
    def hammingDistance(self, x, y):
        ans=0
        temp=x^y 
        while temp!=0:
            temp=temp&(temp-1)
            ans+=1
        return ans