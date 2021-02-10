class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2:  return True
        left2right = 0
        curMin = -float('inf')
        for i in range(len(nums)):
            if curMin <= nums[i]:
                curMin = nums[i]
            else:
                left2right += 1

        right2left = 0
        curMax = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            if curMax >= nums[i]:
                curMax = nums[i]
            else:
                right2left += 1
        return min(left2right, right2left) <= 1
        