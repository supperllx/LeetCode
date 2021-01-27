class UnionFind:
    def __init__(self):
        self.d = dict()

    def find(self, point):
        if point not in self.d: self.d[point] = point
        elif self.d[point] != point:
            self.d[point] = self.find(self.d[point])
        return self.d[point]
    
    def connect(self, p1, p2):
        f1, f2 = self.find(p1), self.find(p2)
        if f1 < f2: self.d[f2] = f1
        elif f1 > f2:   self.d[f1] = f2
    

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        uf = UnionFind()
        n = len(grid)
        for i in range(n): # connect all the border points
            uf.connect((i, 0), (i + 1, 0))
            uf.connect((i, n), (i + 1, n))
            uf.connect((0, i), (0, i + 1))
            uf.connect((n, i), (n, i + 1))
        
        res = 1
        for r in range(n):
            for c in range(n):
                if grid[r][c] == ' ':   continue
                if grid[r][c] == '/':
                    p1, p2 = (r, c + 1), (r + 1, c)
                elif grid[r][c] == '\\':
                    p1, p2 = (r, c), (r + 1, c + 1)
                if uf.find(p1) == uf.find(p2):  res += 1
                else:   uf.connect(p1, p2)
        return res