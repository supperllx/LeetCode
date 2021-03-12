# class Solution:
#     def minCut(self, s: str) -> int:
#         d = set()
#         def find(left, right):
#             while left >= 0 and right < len(s) and s[left] == s[right]:
#                 d.add((left, right))
#                 left -= 1
#                 right += 1
#         for i in range(len(s)):
#             find(i, i)
#             if i < len(s) - 1:
#                 find(i, i + 1)
#         res = float('inf')
#         def dfs(i, count):
#             nonlocal res
#             if i == len(s):
#                 res = min(res, count)
#             if s[i:] == s[i:][::-1]:
#                 res = min(res, count + 1)
#             else:
#                 for j in range(i, len(s)):
#                     if (i, j) in d:
#                         dfs(j + 1, count + 1)
#         dfs(0, 0)
#         return res - 1

class Solution:
    def minCut(self, s: str) -> int:
        d = set()
        def find(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                d.add((left, right))
                left -= 1
                right += 1
        for i in range(len(s)):
            find(i, i)
            if i < len(s) - 1:
                find(i, i + 1)

        dp = [float('inf')] * len(s)
        for i in range(len(s)):
            if (0, i) in d:
                dp[i] = 0
            else:
                for j in range(i):
                    if (j + 1, i) in d:
                        dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]