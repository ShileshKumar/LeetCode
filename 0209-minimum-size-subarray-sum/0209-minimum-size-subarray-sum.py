class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        start=0
        end=0
        sum=0
        ans=float('inf')
        
        while end<n:
            while end<n and sum<target:
                sum=sum+nums[end]
                end+=1

            while start<end and sum>=target:
                ans=min(ans,end-start)
                sum=sum-nums[start]
                start+=1
                
        if ans!=float('inf'):
            return ans
        else:
            return 0