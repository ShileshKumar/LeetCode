class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        pre=0
        curr=0
        for i in range(n):
            temp=max(pre+nums[i],curr)
            pre=curr
            curr=temp
        return temp