class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        k=1
        i=j=0
        zeros=0
        ans=-1
        while j<n:
            if nums[j]==0:
                zeros+=1
            if zeros>k:
                while zeros>k:
                    if nums[i]==0:
                        zeros-=1
                    i+=1
            ans=max(ans,j-i+1)
            j+=1
        return ans-1