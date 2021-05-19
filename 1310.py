# class Solution:
#     def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
#         prefix = [0]
#         for i in range(len(arr)):
#             prefix.append(prefix[-1] ^ arr[i])
#         res = []
#         for Li, Ri in queries:
#             res.append(prefix[Li] ^ prefix[Ri + 1])
#         return res

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] + list(accumulate(arr, operator.xor))
        return [prefix[Li] ^ prefix[Ri + 1] for Li, Ri in queries]