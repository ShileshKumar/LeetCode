class Solution:
    def numRescueBoats(self, p: List[int], k: int) -> int:
        p.sort()
        count=0
        i,j=0,len(p)-1
        while i<=j:
            count+=1
            if p[i]+p[j]<=k:
                i+=1
            j-=1
        return count

        
