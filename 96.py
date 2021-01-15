class Solution:
    def numTrees(self, n: int) -> int:
        @functools.cache
        def func(n):
            if n == 0:  return 1
            if n == 1:  return 1
            res = 0
            for i in range(n):
                res += func(i) * func(n - 1 - i)
            return res
        
        return func(n)