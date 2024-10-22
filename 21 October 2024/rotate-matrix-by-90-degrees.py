class Solution:
    def rotateMatrix(self, matrix):
        n = len(matrix)
        rotated_matrix = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                rotated_matrix[j][n - i - 1] = matrix[i][j]

        for i in range(n):
            for j in range(n):
                matrix[i][j] = rotated_matrix[i][j]