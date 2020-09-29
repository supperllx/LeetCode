class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for j in coins:
                dp[i] = min(dp[i], (dp[i - j] + 1 if i - j >= 0 else float('inf')))
        return dp[amount] if dp[amount] != float('inf') else -1
