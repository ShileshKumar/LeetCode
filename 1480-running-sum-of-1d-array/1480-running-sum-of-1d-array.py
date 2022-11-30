class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=[nums[0]]
        n=len(nums)
        for i in range(1,n):
            sum.append(nums[i]+sum[i-1])
        return sum
        