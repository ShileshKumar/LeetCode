class Solution:
    def convertToTitle(self, n: int) -> str:
        abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ans=""
        while n:
            n=n-1
            ans=abc[n%26]+ans
            n=n//26
        return ans