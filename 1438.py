class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minQue, maxQue = collections.deque(), collections.deque()
        res = 0
        left, right = 0, 0
        while right < len(nums):
            while minQue and minQue[-1] > nums[right]:
                minQue.pop()
            minQue.append(nums[right])
            while maxQue and maxQue[-1] < nums[right]:
                maxQue.pop()
            maxQue.append(nums[right])
            while maxQue[0] - minQue[0] > limit:
                if minQue[0] == nums[left]:
                    minQue.popleft()
                if maxQue[0] == nums[left]:
                    maxQue.popleft()
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res