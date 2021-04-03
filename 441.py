class Solution:
    def arrangeCoins(self, n: int) -> int:
        i, res = 1, 0
        while True:
            if n < i:   return res
            n -= i
            i += 1
            res += 1