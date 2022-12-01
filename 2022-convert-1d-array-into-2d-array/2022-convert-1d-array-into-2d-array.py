class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        mat=[]
        row=[]
        ln=len(original)
        if(ln!=m*n):
            return mat
        
        for i in original:
            row.append(i)
            if len(row)==n:
                mat.append(row)
                row=[]
        return mat