class Solution:
    def countBits(self, n: int) -> List[int]:
        ar=[]
        for i in range(0,n+1):
            x=str(bin(i))
            cnt=x.count('1')
            if '1' in x:
                ar.append(cnt)
            else: 
                ar.append(0)
        return ar