class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return 0
        
        nums.sort()
        diff=[]
        for i in range(1,n):
            diff.append(nums[i]-nums[i-1])
        
        return max(diff)