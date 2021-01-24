class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:    return 0
        p = 1
        res = 1
        temp = 1
        while p < len(nums):
            if nums[p] > nums[p - 1]:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1
            p += 1
        return max(res, temp)
