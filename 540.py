# class Solution:
#     def singleNonDuplicate(self, nums: List[int]) -> int:
#         res = 0
#         for n in nums:  res ^= n
#         return res

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left +((right - left) >> 1)
            # left_odd = (mid  - left) % 2
            right_odd = (right - mid + 1) % 2
            if nums[mid] == nums[mid + 1]:
                if right_odd:   left = mid + 2
                else:   right = mid - 1
            
            elif nums[mid] == nums[mid - 1]:
                if right_odd:    right = mid - 2
                else:   left = mid + 1
            else:   return nums[mid]
            
        return nums[left]

                