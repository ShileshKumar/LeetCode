class Solution:
    def sortSentence(self, s: str) -> str:
        a=s.split(" ")
        d={}
        for i in a:
            d[int(i[-1])]=i[:-1]
        print(d)
        res=''
        c=1
        k1=sorted(d.keys())
        for i in k1:
            res+=d[i]
            res+=' '
        return res[:-1]