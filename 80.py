# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 0:  return 0
#         dd = collections.defaultdict(int)
#         fast, slow = 1, 0
#         dd[nums[slow]] += 1
#         for fast in range(1, n):
#             if dd[nums[fast]] < 2:
#                 slow += 1
#                 nums[slow] = nums[fast]
#                 dd[nums[fast]] += 1
#             else:
#                 dd[nums[fast]] += 1
#                 fast += 1
#         return slow + 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:    return 0
        slow, fast = 0, 1
        count = 1
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                count = 1
                nums[slow] = nums[fast]
            elif count < 2:
                slow += 1
                count += 1
                nums[slow] = nums[fast]
            else:
                count += 1
            fast += 1
        return slow + 1