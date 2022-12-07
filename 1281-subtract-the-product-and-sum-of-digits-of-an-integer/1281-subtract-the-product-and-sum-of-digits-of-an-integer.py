class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        p=1
        s=0
        x=str(n)
        for i in x:
            p=p*int(i)
            s=s+int(i)
            
        return p-s