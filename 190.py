class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        mask = 1
        for _ in range(31):
            if n & mask == 1:
                res += 1
            n >>= 1
            res <<= 1
        return res + (n & mask)
