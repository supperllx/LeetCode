class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if not nums:    return -1
        left, right = 0, sum(nums) - nums[0]
        if left == right:   return 0
        index = 0
        while index < len(nums) - 1:
            index += 1
            left += nums[index - 1]
            right -= nums[index]
            if left == right:   return index
        return -1
            