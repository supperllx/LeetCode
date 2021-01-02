# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         q = deque()
#         res = []
#         i = 0
#         while i < len(nums):
#             while len(q):
#                 if nums[q[-1]] <= nums[i]:
#                     q.pop()
#                 elif i - q[0] == k:
#                     q.popleft()
#                 else:
#                     break
#             q.append(i)
#             res.append(nums[q[0]])
#             i += 1
#         return res[k-1: ]

# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         if n <= k:  return [max(nums)]
#         dq = collections.deque() # stores the indexes of the window
#         res = []

#         for i in range(n):
#             while len(dq):
#                 if nums[dq[-1]] <= nums[i]:
#                     dq.pop()
#                 elif i - dq[0] >= k:
#                     dq.popleft()
#                 else:
#                     break
#             dq.append(i)
#             res.append(nums[dq[0]])
#         return res[k - 1: ]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n <= k:  return [max(nums)]
        hp = [(-num, i) for i, num in enumerate(nums[:k])]
        heapq.heapify(hp)
        res = [-hp[0][0]]

        for i in range(k, n):
            heapq.heappush(hp, (-nums[i], i))
            while i - hp[0][1] >= k:
                heapq.heappop(hp)
            res.append(-hp[0][0])

        return res