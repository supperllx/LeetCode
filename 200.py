# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:  #DFS
#         def dfs(row, col):
#             if grid[row][col] == '1':
#                 grid[row][col] = '2'
#                 if row > 0: dfs(row - 1, col)
#                 if row < len(grid) - 1: dfs(row + 1, col)
#                 if col > 0: dfs(row, col - 1)
#                 if col < len(grid[0]) - 1:   dfs(row, col + 1)
        
#         res = 0
#         for row in range(len(grid)):
#             for col in range(len(grid[0])):
#                 if grid[row][col] == '1':
#                     res += 1
#                     dfs(row, col)
#         return res

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:  #BFS
        def bfs(row, col):
            dq = collections.deque()
            dq.append((row, col))
            grid[row][col] = '2'
            while len(dq):
                    r, c = dq.popleft()
                    if r > 0 and grid[r -1][c] == '1': 
                        dq.append((r - 1, c))
                        grid[r - 1][c] = '2'
                    if r < len(grid) - 1 and grid[r + 1][c] == '1':
                        dq.append((r + 1, c))
                        grid[r + 1][c] = '2'
                    if c > 0 and grid[r][c -1] == '1': 
                        dq.append((r, c - 1))
                        grid[r][c - 1] = '2'
                    if c < len(grid[0]) - 1 and grid[r][c + 1] == '1':
                        dq.append((r, c + 1))
                        grid[r][c + 1] = '2'

        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    res += 1
                    bfs(row, col)
        return res
