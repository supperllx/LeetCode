class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        res = 0
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:    res += matrix[r][c]
                    else:
                        matrix[r][c] = min(matrix[r - 1][c - 1], matrix[r - 1][c], matrix[r][c - 1]) + 1
                        res += matrix[r][c]
        return res