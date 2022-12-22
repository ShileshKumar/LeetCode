class Solution(object):
    def check(self, nums):
        n=len(nums)
        if len(nums)==1: 
            return True
        
        threshold = 0

        for i in range(n-1):
            if nums[i]>nums[i+1]: 
                threshold+=1
                
        if threshold!=0 and nums[0]<nums[-1]:
            return False
        
        if threshold==0 or threshold==1:
            return True 
        
        else:
            return False