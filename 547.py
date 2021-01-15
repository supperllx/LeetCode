# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         visited = set()
#         res = 0
        
#         def dfs(i):
#             nonlocal visited
#             if i not in visited:
#                 visited.add(i)
#                 for j in range(n):
#                     if isConnected[i][j] == 1:  dfs(j)
        
#         for i in range(n):
#             if i not in visited:    res += 1
#             dfs(i)
#         return res

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        res = 0

        def bfs(i):
            nonlocal visited
            dq = collections.deque()
            dq.append(i)
            visited.add(i)

            while len(dq):
                cur = dq.popleft()
                for j in range(n):
                    if j not in visited and isConnected[cur][j] == 1:
                        visited.add(j)
                        dq.append(j)
        
        for i in range(n):
            if i not in visited:
                res += 1
                bfs(i)
        return res