class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n<=1:
                return 1
            else:
                return n*fact(n-1)
        res=str(fact(n))
        m=len(res)
        ans,c0=0,0
        for i in range(m-1,-1,-1):
            if res[i]=='0':
                c0+=1
                ans=max(ans,c0)
            else:
                c0=0
        return ans