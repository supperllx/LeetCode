class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:   
            res = -int(str(x)[1:][::-1])
        else:   
            res = int(str(x)[::-1])
        return res if -(1<<31) <= res <= (1<<31) - 1 else 0 