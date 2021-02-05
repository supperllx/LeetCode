# class Solution:
#     def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
#         suma, sumb = sum(A), sum(B)
#         n = abs(suma - sumb) >> 1
#         sa, sb = set(A), set(B)
#         res = [n + 1, 1] if suma > sumb else [1, n + 1]
#         while True:
#             if res[0] in sa and res[1] in sb:   return res
#             res[0] += 1
#             res[1] += 1

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        suma, sumb = sum(A), sum(B)
        d = (suma - sumb) >> 1
        sa = set(A)
        for ib in B:
            if (ib + d) in sa:  return [ib + d, ib]