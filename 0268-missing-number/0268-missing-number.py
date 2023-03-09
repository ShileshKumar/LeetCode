class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        x=nums[0]
        for i in range(1,n):
            x=x^nums[i]
        
        y=1
        for j in range(2,n+1):
            y=y^j
        
        return x^y