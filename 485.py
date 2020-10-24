class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:  return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        # res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = dp[i -1 ] + 1 if nums[i] == 1 else 0
            # res = max(res, dp[i])
        return max(dp)

# class Solution:
#     def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#         stack = []
#         res = 0
#         for i in nums:
#             if i:   stack.append(i)
#             else:
#                 res = max(res, len(stack))
#                 stack.clear()
#         res = max(res, len(stack))
#         return res