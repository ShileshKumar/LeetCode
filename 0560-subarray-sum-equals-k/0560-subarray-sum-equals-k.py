class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        cnt,sum=0,0
        d={}
        for i in nums:
            sum+=i
            if sum==k:
                cnt+=1
            if (sum-k) in d:
                cnt+=d[sum-k]
            if sum in d:
                d[sum]+=1
            else:
                d[sum]=1
        return cnt
    
