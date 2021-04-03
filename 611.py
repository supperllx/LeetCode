class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for b in range(1, len(nums) - 1):
            for a in range(b):
                res += max(0, (bisect.bisect_left(nums, nums[a] + nums[b]) - 1 - b))
        return res