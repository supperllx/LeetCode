# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         for i in range(len(nums) - 1):
#             if nums[i + 1] < nums[i]: return nums[i + 1]
#         return nums[0]

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if nums[right] > nums[left]:    return nums[0] #just increase
        while left <= right:
            if right - left <= 1:   return min(nums[left], nums[right])
            mid = (left + right) // 2
            if nums[mid] > nums[left]:  left = mid
            elif nums[mid] < nums[right]:   right = mid
