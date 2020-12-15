class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:   return len(nums)
        lastDiff = nums[1] - nums[0]
        res = 2 if lastDiff != 0 else 1
        for i in range(2, len(nums)):
            curDiff = nums[i] - nums[i - 1]
            if (lastDiff <= 0 and curDiff > 0) or (lastDiff >=0 and curDiff < 0):
                res += 1
                lastDiff = curDiff
        
        return res