class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        n=len(nums)
        m=len(queries)
        res=[0]*m
        prefixSum=[]
        sum=0
        for i in range(n):
            sum+=nums[i]
            prefixSum.append(sum)
            
        for i in range(m):
            for j in range(n):
                if prefixSum[j]<=queries[i]:
                    res[i]=j+1
                else:
                    break
        return res