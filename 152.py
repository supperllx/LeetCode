class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp_max = [float('inf')] * n
        dp_min = [float('inf')] * n
        dp_max[0] = nums[0]
        dp_min[0] = nums[0]
        for i in range(1, n):
            dp_max[i] = max(dp_min[i - 1] * nums[i], max(dp_max[i - 1] * nums[i], nums[i]))
            dp_min[i] = min(dp_max[i - 1] * nums[i], min(dp_min[i - 1] * nums[i], nums[i]))
        return max(dp_max)