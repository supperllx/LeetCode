import sortedcontainers
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:   return False
        left = sortedcontainers.SortedList(nums[:1])
        right = sortedcontainers.SortedList(nums[1:])
        i = 1
        while i < len(nums) - 1:
            right.discard(nums[i])
            l = right.bisect_right(left[0])
            r = right.bisect_left(nums[i])
            if l < r:   return True
            left.add(nums[i])
            i += 1
        return False