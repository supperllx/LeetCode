# class Solution:
#     def integerBreak(self, n: int) -> int:
#         dp = [0] * (n + 1)
#         dp[1] = 1
#         dp[2] = 1
#         for i in range(3, n + 1):
#             maxRes = 0
#             for j in range(1, (i // 2) + 1):
#                 maxRes = max([maxRes, j * (i - j), dp[j] * (i - j), j * dp[i - j], dp[j] * dp[i - j]])
#             dp[i] = maxRes
#         return dp[n]

class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:  return n - 1
        a, b = divmod(n, 3)
        if b == 0:  return 3 ** a
        elif b == 1:    return (3 ** (a - 1)) * 4
        else:   return (3 ** a) * 2