class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res=[]
        temp=arr.copy()
        temp.sort()
        d={}
        rank=1
        
        for i in temp:
            if i not in d:
                d[i]=rank
                rank+=1
            
        for i in arr:
            res.append(d[i])
    
        return res