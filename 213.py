# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]
#         res = 0
#         for i in range(n):
#             dp = [0] * n
#             dp[0] = nums[i]
#             dp[1] = max(nums[i], nums[(i + 1) % n])
#             for j in range(2, n):
#                 if j < n - 1:
#                     dp[j] = max(dp[j - 1], dp[j - 2] + nums[(i + j) % n])
#                 else:
#                     if dp[0] == 0:
#                         dp[j] = max(dp[j - 1], dp[j - 2] + nums[(i + j) % n])
#                     else:
#                         dp[j] = dp[j - 1]
#             res = max(res, dp[n - 1])
#         return res

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        res = 0

        def func(nums):
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, n):
                if i < n - 1 or dp[0] == 0:
                    dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
                else:
                    dp[i] = dp[i - 1]
            return dp[n - 1]
        
        return max(func(nums), func(nums[::-1]))