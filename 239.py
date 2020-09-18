class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        i = 0
        while i < len(nums):
            while len(q):
                if nums[q[-1]] <= nums[i]:
                    q.pop()
                elif i - q[0] == k:
                    q.popleft()
                else:
                    break
            q.append(i)
            res.append(nums[q[0]])
            i += 1
        return res[k-1: ]