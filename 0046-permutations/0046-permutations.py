import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, perm):
            if len(perm) == n:
                output.append(perm.copy())
                return
            for i in range(len(nums)):
                perm.append(nums[i])
                new_nums = nums[:i] + nums[i+1:]
                backtrack(new_nums, perm)
                perm.pop()
			
        output = []
        n = len(nums)
        backtrack(nums, [])
        return output