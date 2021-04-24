# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         for i in range(len(nums) - 1):
#             if nums[i + 1] < nums[i]: return nums[i + 1]
#         return nums[0]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # @functools.cache
        def func(left, right):
            if right < left:    return float('inf')
            if left == right:   return nums[left]
            if right - left == 1:   return min(nums[left], nums[right])

            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                return min(nums[left], func(mid + 1, right))
            else:
                return min(nums[mid], func(left, mid - 1))
        return func(0, len(nums) - 1)