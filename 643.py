class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cur_sum = sum(nums[:k - 1])
        res = -float('inf')
        left, right = 0, k - 1
        while right < len(nums):
            cur_sum += nums[right]
            if right - left + 1 > k:
                cur_sum -= nums[left]
                left += 1
            res = max(res, cur_sum / k)
            right += 1
        return res
