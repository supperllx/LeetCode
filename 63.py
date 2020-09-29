class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for i in range(m)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1,n):
            dp[0][i] = dp[0][i-1] - obstacleGrid[0][i]
            dp[0][i] = 0 if dp[0][i] <=0 else 1
        for j in range(1, m):
            dp[j][0] = dp[j-1][0] - obstacleGrid[j][0]
            dp[j][0] = 0 if dp[j][0] <= 0 else 1

        for row in range(1, m):
            for col in range(1, n):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] == 0
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[m-1][n-1]
                
