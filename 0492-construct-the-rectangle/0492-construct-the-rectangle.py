class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(math.sqrt(area)),-1,-1):
            if area%i==0:
                return [area//i,i]
            
