class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if len(matrix) == 0:
            self.prefix = matrix
            return
        n, m = len(matrix), len(matrix[0])
        self.prefix = [[matrix[i][j] for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range( 1 , m ):
                self.prefix[i][j] = self.prefix[i][j] + self.prefix[i][j-1]
        for i in range(m):
            for j in range( 1 , n ):
                self.prefix[j][i] = self.prefix[j][i] + self.prefix[j-1][i]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.prefix[row2][col2]
        elif row1 == 0:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1]
        elif col1 == 0:
            return self.prefix[row2][col2] - self.prefix[row1-1][col2]
        else:
            return self.prefix[row2][col2] - self.prefix[row2][col1-1] - self.prefix[row1-1][col2] + self.prefix[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)