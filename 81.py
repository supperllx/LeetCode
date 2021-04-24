# class Solution:
#     def search(self, nums: List[int], target: int) -> bool:
#         if not nums:    return False
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             while left < right and nums[left] == nums[left + 1]:   left += 1
#             while left < right and nums[right] == nums[right - 1]:   right -= 1
#             mid = (left + right) // 2
#             if nums[mid] == target: return True
#             mid_left = mid
#             while mid_left >= 0 and nums[mid] == nums[mid_left]:
#                 mid_left -= 1
#             mid_right = mid
#             while mid_right < len(nums) and nums[mid] == nums[mid_right]:
#                 mid_right += 1
#             if nums[left] <= nums[mid]:
#                 if nums[left] <= target < nums[mid]:
#                     right = mid_left
#                 else:
#                     left = mid_right
#             else:
#                 if nums[mid] < target <= nums[right]:
#                     left = mid_right
#                 else:
#                     right = mid_left
#         return False

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[left + 1]:    left += 1
            while left < right and nums[right] == nums[right - 1]:  right -= 1
            mid = (left + right) // 2
            if nums[mid] == target: return True
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:    right = mid - 1
                else:   left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:   left = mid + 1
                else:   right = mid - 1
        return False