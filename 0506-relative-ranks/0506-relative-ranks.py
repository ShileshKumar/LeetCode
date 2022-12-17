class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d={}
        a=score.copy()
        a.sort(reverse=True)
        for i in range(len(a)):
            if i==0:
                d[a[i]]="Gold Medal"
            elif i==1:
                d[a[i]]="Silver Medal"
            elif i==2:
                d[a[i]]="Bronze Medal"
            else:
                d[a[i]]=len(d)+1
        res=[]
        for i in score:
            res.append(str(d[i]))
        return res

