class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        curEnd = 0
        res = 0
        for t in timeSeries:
            curEnd = max(curEnd, t)
            estimatedEnd = t + duration
            if curEnd <= estimatedEnd:
                res += (estimatedEnd - curEnd)
                curEnd = estimatedEnd
        return res