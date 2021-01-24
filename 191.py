# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         return bin(n).count('1')

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         mask = 1
#         while n:
#             if (n & mask) == 1:
#                 res += 1
#             n >>= 1
#         return res


class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= (n - 1)
        return res