class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n-1):
            if nums[i]!=nums[i+1] and i%2==0:
                return nums[i]
        return nums[-1]