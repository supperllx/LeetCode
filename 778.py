class UnionFind:
    def __init__(self):
        self.d = dict()
    def find(self, p):
        if p not in self.d: self.d[p] = p
        elif self.d[p] != p:
            self.d[p] = self.find(self.d[p])
        return self.d[p]
    def union(self, p1, p2):
        f1, f2 = self.find(p1), self.find(p2)
        if f1 < f2: self.d[f2] = f1
        elif f1 > f2:   self.d[f1] = f2

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        uf = UnionFind()
        hp = []
        for r in range(m := len(grid)):
            for c in range(n := len(grid[0])):
                global_id = r * n + c
                if r > 0:
                    neighbor_id = global_id - n
                    heapq.heappush(hp, (max(grid[r][c], grid[r - 1][c]), global_id, neighbor_id))
                if c > 0:
                    neighbor_id = global_id - 1
                    heapq.heappush(hp, (max(grid[r][c], grid[r][c - 1]), global_id, neighbor_id))
        
        startID, endID = 0, m * n - 1
        t = -1
        while uf.find(startID) != uf.find(endID):
            t += 1
            while hp and hp[0][0] <= t:
                e = heapq.heappop(hp)
                uf.union(e[1], e[2])
        return t


