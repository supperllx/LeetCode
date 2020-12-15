class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        d = {}
        for i in range(len(equations)):
            d[(equations[i][0], equations[i][1])] = values[i]

        graph = collections.defaultdict(set)
        v = {}
        for index, equ in enumerate(equations):
            graph[equ[0]].add(equ[1])
            graph[equ[1]].add(equ[0])
            v[(equ[0], equ[1])] = values[index]
            v[(equ[1], equ[0])] = float(1 / values[index])

        visited = set()
        # def dfs(start, end):
        #     nonlocal visited
        #     if start in visited:    return 0
        #     if (start, end) in v:   return v[(start, end)]
        #     if start not in graph or end not in graph:    return 0
        #     visited.add(start)
        #     for neighbor in graph[start]:
        #         temp = dfs(neighbor, end) * v[(start, neighbor)]
        #         if temp != 0: 
        #             visited.remove(start)
        #             v[(start, end)] = temp
        #             v[(end, start)] = float(1 / temp)
        #             return temp
        #     visited.remove(start)
        #     return 0

        def dfs(start, end):
            nonlocal visited
            if start not in graph or end not in graph:  return 0
            if start == end:    return 1.0
            if start in visited:    return 0
            if (start, end) in v:   return v[(start, end)]
            visited.add(start)
            for neighbor in graph[start]:
                temp_res = dfs(neighbor, end) * v[(start, neighbor)]
                if temp_res: 
                    v[(start, end)] = temp_res
                    v[(end, start)] = float(1 / temp_res)
                    break
            visited.remove(start)
            return temp_res

        res = []
        for q in queries:
            vq = dfs(q[0], q[1])
            res.append(float(vq) if vq != 0 else -1.0) 
        return res




