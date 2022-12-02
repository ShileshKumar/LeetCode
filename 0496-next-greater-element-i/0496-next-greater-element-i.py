class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        flag = 0
        for i in range(len(nums1)):
            if nums2.index(nums1[i])!=-1:
                ind = nums2.index(nums1[i])
                
                while ind != len(nums2):
                    if nums2[ind] > nums1[i]:
                        res.append(nums2[ind])
                        flag = 1
                        break
                    ind+=1
                if flag == 0:
                    res.append(-1)
                
                flag = 0
            else:
                res.append(-1)          
        return res
