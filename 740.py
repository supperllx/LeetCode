# class Solution:
#     def deleteAndEarn(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         n = max(nums)
#         arr = [0] * (n + 1)
#         for i in nums:
#             arr[i] += 1
        
#         dp = [0] * (n + 1)
#         dp[0] = 0 * arr[0]
#         dp[1] = max(dp[0], 1 * arr[1])

#         for i in range(2, n + 1):
#             dp[i] = max(dp[i - 1], dp[i - 2] + i * arr[i])
#         return dp[n]

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        ct = collections.Counter(nums)
        arr = sorted(ct.keys())
        n = max(arr)

        dp = [0] * len(arr)
        dp[0] = arr[0] * ct[arr[0]]
        dp[1] = max(dp[0], arr[1] * ct[arr[1]]) if arr[1] - arr[0] == 1 else dp[0] + arr[1] * ct[arr[1]]
        for i in range(2, len(arr)):
            if arr[i] - arr[i - 1] > 1:
                dp[i] = dp[i - 1] + arr[i] * ct[arr[i]]
            else:
                dp[i] = max(dp[i - 1], dp[i - 2] + arr[i] * ct[arr[i]])
        return dp[-1]