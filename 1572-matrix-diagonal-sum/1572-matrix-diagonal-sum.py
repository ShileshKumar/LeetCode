class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary_diagonal_sum,secondary_diagonal_sum=0,0
        n=len(mat)
        for i in range(n):
            primary_diagonal_sum+=mat[i][i]
            secondary_diagonal_sum+=mat[n-i-1][i]
        print(primary_diagonal_sum,secondary_diagonal_sum)
        if n%2!=0:
            mid=mat[n//2][n//2]
            return primary_diagonal_sum+secondary_diagonal_sum-mid
        else:
            return primary_diagonal_sum+secondary_diagonal_sum