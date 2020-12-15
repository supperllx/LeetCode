# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int: #nlogn
#         if not nums:    return 0
#         nums.sort()
#         res = 0
#         temp = 1
#         for i in range(1, len(nums)):
#             if nums[i] - nums[i - 1] == 1:
#                 temp += 1
#             elif nums[i] - nums[i - 1] > 1:
#                 res = max(res, temp)
#                 temp = 1
#         res = max(res, temp)
#         return res

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            if n - 1 not in s:
                temp = 1
                while n + 1 in s:
                    temp += 1
                    n += 1
                res = max(res, temp)
        return res


