class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        cur_sum = 0
        left, right = 0, 0
        res = float('inf')

        while right < len(nums):
            cur_sum += nums[right]
            if cur_sum >= s:
                while left < right:
                    if cur_sum - nums[left] >= s:
                        cur_sum -= nums[left]
                        left += 1
                    else:
                        break
                res = min(res, right - left + 1)
            right += 1
        return res if res != float('inf') else 0