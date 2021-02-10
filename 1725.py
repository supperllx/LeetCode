class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        res = 0
        for l, w in rectangles:
            if maxLen == min(l, w):
                res += 1
            elif maxLen < min(l, w):
                maxLen = min(l, w)
                res = 1
        return res
