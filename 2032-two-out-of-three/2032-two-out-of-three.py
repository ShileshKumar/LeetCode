class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        ans = set()
        for num in nums1:
            if num in nums2 or num in nums3: 
                ans.add(num)

        for num in nums2:
            if num in nums1 or num in nums3: 
                ans.add(num)
                
        for num in nums3:
            if num in nums1 or num in nums2: 
                ans.add(num)
                
        return list(ans)
        