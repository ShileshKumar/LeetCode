class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1: return 0
        min_diff=float("inf")
        index=-1
        left,right=0,sum(nums)
        
        for i in range(n):
            left+=nums[i]
            right-=nums[i]
            left_avg=left//(i+1)
            
            if i==n-1: 
                right_avg=0
            else:
                right_avg=right//(n-i-1)
            avg_diff=abs(right_avg-left_avg)
            
            if avg_diff<min_diff:
                min_diff=avg_diff
                index=i
        return index