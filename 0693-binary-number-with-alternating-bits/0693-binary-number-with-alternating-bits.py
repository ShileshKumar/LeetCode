class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x=bin(n)[2:]
        y=len(x)
        for i in range(1,y):
            if x[i]==x[i-1]:
                return False
        return True