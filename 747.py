class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        max1 = max(nums)
        i1 = nums.index(max1)
        max2 = max(nums[:i1] + nums[i1 + 1:])
        if max1 >= 2 * max2:
            return i1
        else:
            return -1