class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        out = []
        for i in range(len(matrix)):
            for k in range(len(matrix[i])):
                if matrix[i][k] == 0:
                    out.append([i,k])
        for item in out:
            for a in range(len(matrix[item[0]])):
                matrix[item[0]][a] = 0
            for b in range(len(matrix)):
                matrix[b][item[1]] = 0
            
        return matrix
        