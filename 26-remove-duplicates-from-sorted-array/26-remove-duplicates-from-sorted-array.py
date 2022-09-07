class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return
        c=nums[0]
        i=1
        while(i<n):
            if c==nums[i]:
                nums.pop(i)
                n=n-1
            else:
                c=nums[i]
                i+=1
     