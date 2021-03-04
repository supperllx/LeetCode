# class Solution:
#     def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
#         if not envelopes:
#             return 0
#         envelopes.sort(key = lambda e: (e[0], -e[1]))
#         n = len(envelopes)
#         dp = [1] * n
#         for i in range(1, n):
#             for j in range(i):
#                 if envelopes[j][1] < envelopes[i][1]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key = lambda e: (e[0], -e[1])) # w increasing, h decreasing
        dp = []
        for w, h in envelopes:
            if not dp or dp[-1] < h:
                dp.append(h)
            else:
                index = bisect.bisect_left(dp, h)
                dp[index] = min(dp[index], h)
        return len(dp)