# class Solution:
#     def isPowerOfTwo(self, n: int) -> bool:
#         i = 1
#         while i <= n:
#             if i == n:  return True
#             i <<= 1
#         return False

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # n & (n - 1): set the rightest '1' to '0'
        return n > 0 and n & (n - 1) == 0