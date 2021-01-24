class Solution:
    def countBits(self, num: int) -> List[int]:
        # def func(n):
        #     res = 0
        #     mask = 1
        #     while n:
        #         if (n & mask) == 1: res += 1
        #         n >>= 1
        #     return res
        
        def func(n):
            res = 0
            while n:
                res += 1
                n &= (n - 1)
            return res
        res = []
        n = 0
        while n <= num:
            res.append(func(n))
            res.append(res[-1] + 1)
            n += 2
        return res if num % 2 == 1 else res[:-1]
            
