# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         res = 1
#         def func(arr, path):
#             nonlocal res
#             if len(arr) == 1:
#                 if not path:    return 
#                 else:
#                     if arr[0] > path[-1]:   res = max(res, len(path) + 1)
#             else:
#                 for i in range(len(arr)):
#                     if not path:    func(arr[i+1: ], path + [arr[i]])
#                     elif arr[i] > path[-1]:
#                         res = max(res, len(path) + 1)
#                         func(arr[i + 1:], path + [arr[i]])

#         func(nums, [])
#         return res

# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         n = len(nums)
#         dp = [1] * n
#         for i in range(1, n):
#             for j in range(i):
#                 if nums[j] < nums[i]:
#                     dp[i] = max(dp[i], dp[j] + 1)
#         return max(dp)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for n in nums:
            if not dp or n > dp[-1]:
                dp.append(n)
            else:
                index = bisect.bisect_left(dp, n)
                dp[index] = min(dp[index], n)
        print(dp)
        return len(dp)