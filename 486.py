# class Solution:
#     def PredictTheWinner(self, nums: List[int]) -> bool:
#         @functools.lru_cache(None)
#         def func(left, right, turn):
#             nonlocal nums
#             if left == right:
#                 return nums[left] * turn
#             else:
#                 pick_left = nums[left] * turn + func(left + 1, right, -turn)
#                 pick_right = nums[right] * turn + func(left, right - 1, -turn)
#                 return max(pick_left, pick_right)
            
#         return func(0, len(nums) - 1, 1) >= 0

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @functools.lru_cache(None)
        def func(left, right):
            nonlocal nums
            if left == right:
                return nums[left]
            else:
                pick_left = nums[left] - func(left + 1, right)
                pick_right = nums[right] - func(left, right - 1)
                return max(pick_left, pick_right)
            
        return func(0, len(nums) - 1) >= 0