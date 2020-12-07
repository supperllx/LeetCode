# class Solution:
#     def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
#         s1 = []
#         s2 = collections.Counter()
#         n = len(A)
#         for i in range(n):
#             for j in range(n):
#                 s1.append(A[i] + B[j])
#                 s2[C[i] + D[j]] += 1
#         res = 0
#         for x in s1:
#             if (0 - x) in s2:   res += s2[0 - x]
#         return res
        
# class Solution:
#     def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
#         s1 = collections.Counter()
#         for na in A:
#             for nb in B:
#                 s1[na + nb] += 1

#         res = 0
#         for nc in C:
#             for nd in D:
#                 if (0 - (nc + nd)) in s1:   res += s1[(0 - (nc + nd))]
#         return res

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ct = collections.Counter(na + nb for na in A for nb in B)
        return sum(ct[0 - nc - nd] for nc in C for nd in D)

