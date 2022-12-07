class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt=0
        ans=0
        n=len(nums)
        for i in range(n):
            if nums[i]==1:
                cnt+=1
                ans=max(ans,cnt)
            else:
                cnt=0
        return ans