class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        res = 0
        s = set()
        for i in J:
            s.add(i)
        for ch in S:
            if ch in s: res += 1
        return res
        