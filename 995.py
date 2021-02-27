# class Solution:
#     def minKBitFlips(self, A: List[int], K: int) -> int:
#         res = 0
#         for i in range(len(A) - K + 1):
#             if A[i] == 0:
#                 res += 1
#                 for j in range(i, i + K):
#                     A[j] ^= 1
#         if A[-K:] == [1] * K:
#             return res
#         else:
#             return -1
        
# class Solution:
#     def minKBitFlips(self, A: List[int], K: int) -> int:
#         res = 0
#         n = len(A)
#         curWindowFlip = 0
#         p = 0
#         while p < n:
#             if p >= K and A[p - K] == 2:
#                 curWindowFlip -= 1
#             if (curWindowFlip % 2 == 0 and A[p] == 0) or (curWindowFlip % 2 == 1 and A[p] == 1):
#                 if p + K > n:
#                     return -1
#                 else:
#                     curWindowFlip += 1
#                     A[p] = 2
#                     res += 1
#             p += 1
#         return res

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        n = len(A)
        res = 0
        curWindowFlip = 0
        for i in range(n):
            if i >= K and A[i - K] == 2:
                curWindowFlip -= 1
            if (curWindowFlip % 2 == 0 and A[i] == 0) or (curWindowFlip % 2 == 1 and A[i] == 1):
                if i + K > n:
                    return -1
                curWindowFlip += 1
                res += 1
                A[i] = 2
        return res
