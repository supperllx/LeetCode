class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        def dfs(path):
            if path[-1] == n - 1:
                res.append(path)
            else:
                for neighbor in graph[path[-1]]:
                    dfs(path + [neighbor])
        dfs([0])
        return res