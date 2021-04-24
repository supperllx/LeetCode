class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(len(dp)):
            for j in range(1, min(nums[i] + 1, len(dp) - i)): # incase i + j >= len(dp)
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]