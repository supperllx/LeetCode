# class Solution:
#     def isPowerOfFour(self, n: int) -> bool:
#         import math
#         return n > 0 and math.log2(n) % 2 == 0

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n > 0 and n & (n - 1) == 0 prove is 2^x; n & 0xaaaaaaaa == 0 prove is not 2^(2k + 1)
        return n > 0 and n & (n - 1) == 0 and n & 0xaaaaaaaa == 0