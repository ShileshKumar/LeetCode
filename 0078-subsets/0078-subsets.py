class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        m=1<<n
        sub=[[] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if (i>>j)&1==1:
                    sub[i].append(nums[j])
        return sub
                