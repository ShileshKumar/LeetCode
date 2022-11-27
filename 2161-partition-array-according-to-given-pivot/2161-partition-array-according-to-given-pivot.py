class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        b=[]
        a=[]
        s=[]
        for i in nums:
            if i<pivot:
                b.append(i)
            elif i==pivot:
                s.append(i)
            else:
                a.append(i)
        return b+s+a