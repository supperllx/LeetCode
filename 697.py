class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for i, n in enumerate(nums):
            if n not in d:
                d[n] = [1, i, i]
            else:
                d[n][0] += 1
                d[n][2] = i
        
        heapq.heapify(hp := [(-t[0], t[2] - t[1] + 1) for t in d.values()])
        return hp[0][1]