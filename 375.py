# class Solution:
#     def getMoneyAmount(self, n: int) -> int:
#         res = float('inf')
#         temp = 0
#         all_used = int('1' * (n - 1), 2)
#         @functools.cache
#         def dfs(used):
#             nonlocal temp, res, all_used
#             if used == all_used:
#                 res = min(res, temp)
#             else:
#                 for i in range(n):
#                     cur_encoded = 1 << i
#                     if cur_encoded & used == 0:
#                         temp += i
#                         dfs(cur_encoded | used)
#                         temp -= i
#         dfs(0)
#         return res

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.cache
        def dfs(left, right):
            if left >= right:
                return 0
            else:
                min_res = float('inf')
                mid  = (left + right) // 2
                for i in range(mid, right + 1):
                    temp = i + max(dfs(left, i - 1), dfs(i + 1, right))
                    min_res = min(min_res, temp)
                return min_res

        return dfs(1, n)
                    
