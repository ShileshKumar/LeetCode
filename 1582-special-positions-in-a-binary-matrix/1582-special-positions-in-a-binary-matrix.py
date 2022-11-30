class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        row=[0]*n
        col=[0]*m
        
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    row[i]+=1
                    col[j]+=1
        
        cnt=0
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1 and row[i]==1 and col[j]==1:
                    cnt+=1
        
        return cnt