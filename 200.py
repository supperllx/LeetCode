# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m, n = len(grid), len(grid[0])
#         def dfs(r, c):
#             if grid[r][c] == '1':
#                 grid[r][c] = '2'
#                 for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
#                     if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
#                         dfs(nr, nc)
#         res = 0
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == '1':
#                     res += 1
#                     dfs(r, c)
#         return res

# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         m, n = len(grid), len(grid[0])
#         visited = set()
#         def bfs(r, c):
#             dq = collections.deque()
#             dq.append((r, c))
#             # grid[r][c] = '2'
#             visited.add((r, c))
#             while dq:
#                 curR, curC = dq.popleft()
#                 for nr, nc in ((curR + 1, curC), (curR - 1, curC), (curR, curC + 1), (curR, curC - 1)):
#                     if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1' and (nr, nc) not in visited:
#                         # grid[nr][nc] = '2'
#                         visited.add((nr, nc))
#                         dq.append((nr, nc))
#         res = 0
#         for r in range(m):
#             for c in range(n):
#                 if grid[r][c] == '1' and (r, c) not in visited:
#                     res += 1
#                     bfs(r, c)
#         return res

class UnionFind:
    def __init__(self):
        self.d = dict()
        self.Count = 0
    def find(self, p):
        if p not in self.d:
            self.d[p] = p
        elif self.d[p] != p:
            self.d[p] = self.find(self.d[p])
        return self.d[p]
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx > fy:
            self.d[fx] = fy
        elif fx < fy:
            self.d[fy] = fx
        self.Count -= 1
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        uf = UnionFind()
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    uf.find((r, c))
                    uf.Count += 1
                    if r > 0 and grid[r - 1][c] == '1' and uf.find((r, c)) != uf.find((r - 1, c)):
                        uf.union((r, c), (r - 1, c))
                    if c > 0 and grid[r][c - 1] == '1' and uf.find((r, c)) != uf.find((r, c - 1)):
                        uf.union((r, c), (r, c - 1))
        return uf.Count