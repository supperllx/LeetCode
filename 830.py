class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        left, right = 0, 1
        res = []
        while right < len(s):
            if s[left] == s[right]:
                right += 1
            else:
                if right - left >= 3:
                    res.append([left, right - 1])
                left = right
                right += 1
        if right - left >= 3:   res.append([left, right - 1])
        return res
