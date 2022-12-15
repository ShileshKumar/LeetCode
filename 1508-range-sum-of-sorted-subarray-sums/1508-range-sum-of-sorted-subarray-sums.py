class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n=len(nums)
        ans=[]
        for i in range(n):
            curr=0
            for j in range(i,len(nums)):
                curr+=nums[j]
                ans.append(curr)
        ans.sort()
        return sum(ans[left-1:right])%(10**9+7)