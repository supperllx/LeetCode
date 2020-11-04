class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        for intval in intervals:
            if len(res) == 0 or intval[0] > res[-1][1]:
                res.append(intval)
            else:
                res[-1][1] = max(res[-1][1], intval[1])
        return res