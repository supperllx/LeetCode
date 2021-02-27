class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        n = len(timePoints)
        if n > 1440: # 24 * 60
            return 0
        timePoints.sort()
        res = float('inf')
        for i in range(n):
            t1 = list(map(int, timePoints[i % n].split(':')))
            t2 = list(map(int, timePoints[(i + 1) % n].split(':')))
            if t2[0] < t1[0]:
                t2[0] += 23
                t2[1] += 60
            diff = abs((t2[0] * 60 + t2[1]) - (t1[0] * 60 + t1[1]))
            res = min(res, diff)
        return res