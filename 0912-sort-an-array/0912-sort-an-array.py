class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #n=len(nums)//2
        if len(nums)>1:
            p=len(nums)//2
            left=nums[:p]
            right=nums[p:]
            
            self.sortArray(left)
            self.sortArray(right)
            
            i=0
            j=0
            k=0
            
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    nums[k]=left[i]
                    i+=1
                    k+=1
                else:
                    nums[k]=right[j]
                    j+=1
                    k+=1
            
            while i<len(left):
                nums[k]=left[i]
                i+=1
                k+=1
            
            while j<len(right):
                nums[k]=right[j]
                j+=1
                k+=1
            
        return nums