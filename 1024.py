class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        max_end = [0] * T
        for i, end in clips:
            if i < T:   max_end[i] = max(max_end[i], end)
        last_pos = 0
        most_right = 0
        res = 0
        for i, end in enumerate(max_end):
            most_right = max(end, most_right)
            if i == last_pos:
                res += 1
                last_pos = most_right
            if i == most_right: return -1
        return res
        