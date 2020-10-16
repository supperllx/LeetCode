class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp= [1]
        p1, p2, p3 = 0, 0, 0
        for i in range(1, n):
            ugly = min(dp[p1] * 2, dp[p2] * 3, dp[p3] * 5)
            dp.append(ugly)
            if ugly == dp[p1] * 2:  p1 += 1
            if ugly == dp[p2] * 3:  p2 += 1
            if ugly == dp[p3] * 5:  p3 += 1
        return dp[-1]