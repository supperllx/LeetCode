class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:    return 0
        min_price = [0] * len(prices)
        dp = [0] * len(prices)
        min_price[0] = prices[0]
        dp[0] = 0
        for i in range(1, len(prices)):
            min_price[i] = min(prices[i], min_price[i-1])
            dp[i] = max(dp[i-1], prices[i] - min_price[i])
        return dp[-1]
