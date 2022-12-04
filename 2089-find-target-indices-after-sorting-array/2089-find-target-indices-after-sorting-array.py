class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n):
            if nums[i]==target:
                res.append(i)
        return res