class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        r1=[0]*n
        c1=[0]*m
        r0=[0]*n
        c0=[0]*m
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    r0[i]+=1
                    c0[j]+=1
                else:
                    r1[i]+=1
                    c1[j]+=1
                    
        for i in range(n):
            for j in range(m):
                grid[i][j]=r1[i]+c1[j]-c0[j]-r0[i]
        
        return grid