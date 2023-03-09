class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n=len(strs)
        d={}
        res=[]
        for i in strs:
            x="".join(sorted(i))
            if x not in d:
                d[x]=[i]
            else:
                d[x].append(i)
                
        for key,value in d.items():
            res.append(value)
        
        return res
            