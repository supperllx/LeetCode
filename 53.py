# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         res = -float('inf')
#         def func(array):
#             nonlocal res
#             if len(array) == 1: 
#                 res = max(res, array[0])
#                 return array[0]
#             else:
#                 temp = max(func(array[:-1]) + array[-1], array[-1])
#                 res = max(res, temp)
#                 return temp
#         func(nums)
#         return res

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        # res = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            # res = max(dp[i], res)
        return max(dp)