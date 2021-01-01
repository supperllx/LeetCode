class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:   return 0
        heapq.heapify(intervals)
        res = 0
        last = heapq.heappop(intervals)
        while len(intervals):
            cur = heapq.heappop(intervals)
            if cur[0] >= last[1]:
                last = cur
            elif last[0] < cur[0] and cur[1] < last[1]:
                last = cur
                res += 1
            else:
                res += 1
        return res