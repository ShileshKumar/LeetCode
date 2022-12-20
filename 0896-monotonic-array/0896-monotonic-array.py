class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        check = self.increasing(nums,n) or self.decreasing(nums,n) 
        if check:
            return True
        else:
            return False
    def increasing(self,nums,n):
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                return False
        return True
    
    def decreasing(self,nums,n):
        for i in range(n-1):
            if nums[i]<nums[i+1]:
                return False
        return True
    
        