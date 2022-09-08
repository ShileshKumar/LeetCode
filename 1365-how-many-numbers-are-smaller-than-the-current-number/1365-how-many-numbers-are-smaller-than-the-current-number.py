#import operator
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            c=0
            e=nums[i]
            for j in range(len(nums)):
                if nums[j]<e:
                    c+=1
            ans.append(c)
        return ans