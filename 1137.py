class Solution:
    def tribonacci(self, n: int) -> int:
        d = {0:0, 1:1, 2:1}
        def func(n: int) -> int:
            nonlocal d
            if n in d:
                return d[n]
            else:
                res = func(n-1) + func(n-2) + func(n-3)
                d[n] = res
                return res
        return func(n)