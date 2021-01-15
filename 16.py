# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         margin = float('inf')
#         res = None
#         def func(arr, path, k):
#             nonlocal margin, res
#             if k == 0:
#                 if (temp_margin := abs(target - path)) < margin:
#                     res = path
#                     margin = temp_margin
#             else:
#                 for i in range(len(arr)):
#                     func(arr[i + 1: ], path + arr[i], k - 1)
#         func(nums, 0, 3)
#         return res

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = float('inf')
        for ia in range(len(nums)):
            ib, ic = ia + 1, len(nums) - 1
            while ib < ic:
                cur = nums[ia] + nums[ib] + nums[ic]
                if cur == target:   return cur
                elif cur < target:
                    ib += 1
                else:
                    ic -= 1
                if abs(target - cur) < abs(target - res):   res = cur
        return res


