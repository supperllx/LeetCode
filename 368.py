class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        maxL, maxValue = 1, nums[0]
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > maxL:
                maxL = dp[i]
                maxValue = nums[i]

        path = []
        index = len(dp) - 1
        while index >= 0: # trace back
            if dp[index] == maxL and maxValue % nums[index] == 0:
                path.append(nums[index])
                maxL -= 1
                maxValue = nums[index]
            index -= 1
        return path