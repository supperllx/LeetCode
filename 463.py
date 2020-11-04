class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    res += 4
                    if row > 0 and grid[row - 1][col] == 1: res -= 2
                    if col > 0 and grid[row][col - 1] == 1: res -= 2
        return res