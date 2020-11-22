# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:  #DFS
#         res = 0
#         def dfs(row, col):
#             grid[row][col] = 2
#             temp = 1
#             if row > 0 and grid[row - 1][col] == 1: 
#                 temp += dfs(row - 1, col)
#             if row < len(grid) - 1 and grid[row + 1][col] == 1:
#                 temp += dfs(row + 1, col)
#             if col > 0 and grid[row][col - 1] == 1:
#                 temp += dfs(row, col - 1)
#             if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
#                 temp += dfs(row, col + 1)
#             return temp
        
#         for r in range(len(grid)):
#             for c in range(len(grid[0])):
#                 if grid[r][c] == 1:
#                     res = max(res, dfs(r, c))
#         return res

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:  #BFS
        def bfs(row, col):
            area = 0
            dq = collections.deque()
            dq.append((row, col))
            grid[row][col] = 2
            while len(dq):
                r, c = dq.popleft()
                area += 1
                if r > 0 and grid[r - 1][c] == 1:
                    dq.append((r - 1, c))
                    grid[r - 1][c] = 2
                if r < len(grid) - 1 and grid[r + 1][c] == 1:
                    dq.append((r + 1, c))
                    grid[r + 1][c] = 2
                if c > 0 and grid[r][c - 1] == 1:
                    dq.append((r, c - 1))
                    grid[r][c - 1] = 2
                if c < len(grid[0]) - 1 and grid[r][c + 1] == 1:
                    dq.append((r, c + 1))
                    grid[r][c + 1] = 2
            return area
            
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res = max(res, bfs(row, col))
        return res
                
