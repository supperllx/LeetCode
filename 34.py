# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]: # O(n)
#         res = []
#         for i in range(len(nums)):
#             if nums[i] == target:
#                 res.append(i)
#                 while i < len(nums) and nums[i] == target:    
#                     i += 1
#                 res.append(i - 1)
#                 return res
#         return [-1, -1]
        
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: # O(log n)
        n = len(nums)
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                p1, p2 = mid - 1, mid + 1
                while p1 >= 0 and nums[p1] == nums[mid]:   p1 -= 1
                while p2 <= n - 1 and nums[p2] == nums[mid]:   p2 += 1
                return [p1 + 1, p2 - 1]
            elif target < nums[mid]:
                right = mid
                while right >= left and nums[right] == nums[mid]:   right -= 1
            elif target > nums[mid]:
                left = mid
                while left <= right and nums[left] == nums[mid]:    left += 1
        return [-1, -1]
        