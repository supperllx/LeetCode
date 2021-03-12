# class Solution:
#     def destCity(self, paths: List[List[str]]) -> str:
#         dd = collections.defaultdict(list)
#         for u, v in paths:
#             dd[u].append(v)
        
#         res = []
#         def dfs(curCity, path):
#             nonlocal res
#             if curCity not in dd:
#                 path
#                 if len(path) >= len(res):
#                     res = path + [curCity]
#             else:
#                 for neighbor in dd[curCity]:
#                     dfs(neighbor, path + [curCity])
#         dfs()

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        s = set()
        for u, v in paths:
            s.add(u)
        for u, v in paths:
            if v not in s:
                return v