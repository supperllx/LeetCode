class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        for r in range(m):
            i = 0
            while r + i < m and i < n:
                if matrix[r + i][i] != matrix[r][0]:
                    return False
                i += 1
        
        for c in range(n):
            j = 0
            while j < m and c + j < n:
                if matrix[j][c + j] != matrix[0][c]:
                    return False
                j += 1
        
        return True