class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        cur = first
        res = [first]
        for i in encoded:
            cur ^= i
            res.append(cur)
        return res