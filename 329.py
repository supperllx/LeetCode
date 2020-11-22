class Solution:
    import functools
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:    return 0
        n_row = len(matrix)
        n_col = len(matrix[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        @lru_cache(None)
        def dfs(x, y):
            best = 1
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if 0 <= new_x <= n_row - 1 and 0 <= new_y <= n_col - 1 and matrix[x][y] < matrix[new_x][new_y]:
                    best = max(best, dfs(new_x, new_y) + 1)
            return best       

        res = 0
        for row in range(n_row):
            for col in range(n_col):
                res = max(res, dfs(row, col))
        return res