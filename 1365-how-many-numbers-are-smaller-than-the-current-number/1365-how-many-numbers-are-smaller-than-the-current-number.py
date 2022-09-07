#import operator
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        x=nums.copy()
        for i in nums:
            x.remove(i)
            #print(x)
            #print(nums)
            c=0
            for j in x:
                if j<i:
                    c+=1
            ans.append(c)
            x=nums.copy()
        return ans