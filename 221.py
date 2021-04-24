class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        maxL = 0
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == '1':
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = min(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + 1
                    maxL = max(maxL, dp[r][c])
        return maxL ** 2