class Solution:
    def numDecodings(self, s: str) -> int:
        s = '0' + s
        dp = [1] * (len(s))
        for i in range(1, len(s)):
            if 10 <= int(s[i - 1: i + 1]) <= 26:
                if s[i] == '0': dp[i] = dp[i - 2]
                else:   dp[i] = dp[i - 1] + dp[i - 2]
            else:
                if s[i] == '0': return 0
                else:   dp[i] = dp[i - 1]

        return dp[-1]

    