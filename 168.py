class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n:
            n, r = divmod(n, 26)
            if r == 0:
                r = 26
                n -= 1
            res = chr(64 + r) + res
        return res

