# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = set()
#         def func(arr, last_sum, path):
#             nonlocal res
#             if len(arr) and last_sum < target:
#                 for i in range(len(arr)):
#                     if last_sum + arr[i] == target:
#                         res.add(tuple(sorted(path + [arr[i]])))
#                     else:
#                         func(arr[i + 1: ], last_sum + arr[i], path + [arr[i]])
#         func(candidates, 0, [])
#         return res

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def func(arr, last_sum, path):
            nonlocal res
            i = 0
            while i < len(arr):
                cur = last_sum + arr[i]
                if cur == target:
                    res.append(path + [arr[i]])
                elif cur < target:
                    func(arr[i + 1: ], cur, path + [arr[i]])
                while i < len(arr) - 1 and arr[i] == arr[i + 1]:    i += 1
                i += 1
        func(candidates, 0, [])
        return res