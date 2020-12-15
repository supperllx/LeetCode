class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        if N < 10:  return N
        arr = [int(i) for i in str(N)]
        dp = [0] * len(arr)
        dp[0] = arr[0]
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                dp[i - 1] -= 1
                dp[i] = 9
                dp[i:] = [9] * (len(dp) - i)
                for j in range(i - 1, 0, -1):
                    if dp[j] < dp[j - 1]:
                        dp[j] = 9
                        dp[j - 1] -= 1
                break
            else:
                dp[i] = arr[i]
        res = 0
        for n in dp:
            res = 10 * res + n
        return res
        