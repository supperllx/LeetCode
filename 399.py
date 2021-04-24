# class Solution:
#     def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
#         # transfer equations from list to dict
#         d = {}
#         for i in range(len(equations)):
#             d[(equations[i][0], equations[i][1])] = values[i]

#         # build graph and dict of values
#         graph = collections.defaultdict(set)
#         v = {}
#         for index, equ in enumerate(equations):
#             graph[equ[0]].add(equ[1])
#             graph[equ[1]].add(equ[0])
#             v[(equ[0], equ[1])] = values[index]
#             v[(equ[1], equ[0])] = float(1 / values[index])

#         # prevent loop in graph
#         visited = set()
#         # def dfs(start, end):
#         #     nonlocal visited
#         #     if start in visited:    return 0
#         #     if (start, end) in v:   return v[(start, end)]
#         #     if start not in graph or end not in graph:    return 0
#         #     visited.add(start)
#         #     for neighbor in graph[start]:
#         #         temp = dfs(neighbor, end) * v[(start, neighbor)]
#         #         if temp != 0: 
#         #             visited.remove(start)
#         #             v[(start, end)] = temp
#         #             v[(end, start)] = float(1 / temp)
#         #             return temp
#         #     visited.remove(start)
#         #     return 0

#         def dfs(start, end):
#             nonlocal visited
#             # since 0.0 < values[i] <= 20.0, we could use 0 as the flag of fail
#             if start not in graph or end not in graph:  return 0
#             if start == end:    return 1.0
#             if start in visited:    return 0
#             if (start, end) in v:   return v[(start, end)]
#             visited.add(start)
#             for neighbor in graph[start]:
#                 temp_res = dfs(neighbor, end) * v[(start, neighbor)]
#                 if temp_res: 
#                     v[(start, end)] = temp_res
#                     v[(end, start)] = float(1 / temp_res)
#                     break
#             visited.remove(start)
#             return temp_res

#         res = []
#         for q in queries:
#             vq = dfs(q[0], q[1])
#             res.append(float(vq) if vq != 0 else -1.0) 
#         return res

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = dict()
        s = set()
        for i in range(len(equations)):
            graph[(equations[i][0], equations[i][1])] = values[i]
            graph[(equations[i][1], equations[i][0])] = 1 / values[i]
            s.add(equations[i][0])
            s.add(equations[i][1])
        
        for k in s:
            for i in s:
                for j in s:
                    if (i, k) in graph and (k, j) in graph:
                        graph[(i, j)] = graph[(i, k)] * graph[(k, j)]
        res = []
        for q in queries:
            if (q[0], q[1]) in graph:
                res.append(graph[(q[0], q[1])])
            else:
                res.append(-1)
        return res