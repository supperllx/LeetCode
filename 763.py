class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_pos = [0] * 26
        for i, ch in enumerate(S):
            last_pos[ord(ch) - 97] = i
        res = []
        start = end = 0
        for i, ch in enumerate(S):
            end = max(end, last_pos[ord(ch) - 97])
            if i == end:
                res.append(end - start + 1)
                start = end + 1
        return res