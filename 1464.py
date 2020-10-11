class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        min_n = [0] * n
        max_n = [0] * n
        min_n[0] = nums[0]
        max_n[0] = nums[0]
        for i in range(1, n):
            # dp[i] = max(dp[i -1], (min(nums[:i]) - 1)*(nums[i] -1), (max(nums[:i]) - 1)*(nums[i] - 1))
            min_n[i] = min(min_n[i - 1], nums[i])
            max_n[i] = max(max_n[i - 1], nums[i])
            dp[i] = max(dp[i -1], (min_n[i - 1] - 1)*(nums[i] - 1), (max_n[i - 1] - 1)*(nums[i] - 1))
        return dp[-1]