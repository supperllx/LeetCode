# class Solution:
#     def closedIsland(self, grid: List[List[int]]) -> int:
#         row = len(grid)
#         col = len(grid[0])
#         directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
#         def dfs(x, y, k):
#             nonlocal grid
#             if grid[x][y] == 0:
#                 grid[x][y] = k
#                 for dx, dy in directions:
#                     if 0 <= (new_x := x + dx) <= row - 1 and 0 <= (new_y := y + dy) <= col - 1:
#                         dfs(new_x, new_y, k)
        
#         for r in [0, row - 1]:
#             for c in range(col):
#                 if grid[r][c] == 0: dfs(r, c, 1)
#         for c in [0, col - 1]:
#             for r in range(row):
#                 if grid[r][c] == 0: dfs(r, c, 1)
        
#         res = 0
#         for r in range(1, row - 1):
#             for c in range(1, col - 1):
#                 if grid[r][c] == 0:
#                     res += 1
#                     dfs(r, c, 2)
#         return res

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def bfs(x, y, k):
            nonlocal grid
            dq = collections.deque()
            dq.append((x, y))
            grid[x][y] = k
            while dq:
                cur_x, cur_y = dq.popleft()
                for dx, dy in directions:
                    if 0 <= (new_x := cur_x + dx) <= row - 1 and 0 <= (new_y := cur_y + dy) <= col - 1 and grid[new_x][new_y] == 0:
                        grid[new_x][new_y] = k
                        dq.append((new_x, new_y))
        
        for r in [0, row - 1]:
            for c in range(col):
                if grid[r][c] == 0: bfs(r, c, 1)
        for c in [0, col - 1]:
            for r in range(row):
                if grid[r][c] == 0: bfs(r, c, 1)
        
        res = 0
        for r in range(1, row - 1):
            for c in range(1, col - 1):
                if grid[r][c] == 0:
                    res += 1
                    bfs(r, c, 2)
        return res