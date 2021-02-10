class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curHeight = 0
        maxHeight = 0
        for g in gain:
            curHeight += g
            maxHeight = max(maxHeight, curHeight)
        return maxHeight