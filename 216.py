# class Solution:
#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         res = []
#         arr = [1] * 9
#         s = set()

#         def func(k, path):
#             nonlocal arr
#             if k == 0 and sum(path) == n: 
#                 nonlocal s
#                 temp_s = ''.join([str(i) for i in arr])
#                 if temp_s not in s:
#                     nonlocal res
#                     res.append(path)
#                     s.add(temp_s)
#             elif k > 0:
#                 for i in range(1, 10):
#                     index = i - 1
#                     if arr[index] == 0: continue
#                     else:
#                         arr[index] = 0
#                         func(k - 1, path + [i])
#                         arr[index] = 1
#         func(k, [])
#         return res

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def func(n, start, path):
            if len(path) == k and n == 0:
                nonlocal res
                res.append(path)
            elif len(path) < k and n > 0:
                for i in range(start, 10):
                    func(n - i, i + 1, path + [i])
        func(n, 1, [])
        return res