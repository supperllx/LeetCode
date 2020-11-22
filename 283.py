# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         if len(nums) == 0:  return 0
#         i = j = 0
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 nums[j] = nums[i]
#                 j+=1
#         for i in range(j, len(nums)):
#             nums[i] = 0

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        p1 = p2 = 0
        while p1 < len(nums):
            if nums[p1] != 0:
                nums[p2] = nums[p1]
                p2 += 1
            p1 += 1
        for i in range(p2, len(nums)):
            nums[i] = 0
