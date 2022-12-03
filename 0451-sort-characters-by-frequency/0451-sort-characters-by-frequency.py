class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
                
        fre=[]
        for k,v in d.items():
            if v not in fre:
                fre.append(v)
        
        ans=''
        fre.sort(reverse=True)
        for j in fre:
            for k in d:
                if j==d[k]:
                    for x in range(j):
                        ans+=k
        return ans