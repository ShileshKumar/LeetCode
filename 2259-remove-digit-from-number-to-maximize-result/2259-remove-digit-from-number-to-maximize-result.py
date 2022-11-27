class Solution:
    def removeDigit(self, num: str, d: str) -> str:
        l=[]
        n=len(num)
        for i in range(n):
            if num[i]==d:
                l.append(int(''.join(num[:i]+num[i+1:])))
        return str(max(l))
            