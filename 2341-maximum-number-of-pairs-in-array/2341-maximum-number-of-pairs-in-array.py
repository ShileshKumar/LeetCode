class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        n=len(nums)
        d={}
        ans=[]
        pairs=0
        remaining=0
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for k,v in d.items():
            if v%2==0:
                pairs+=v//2
            else:
                while v>=2:
                    v=v//2
                    pairs+=1
                remaining+=1
        return [pairs,remaining]
