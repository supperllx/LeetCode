class UnionFind:
    def __init__(self):
        self.f = dict()
    def find(self, p):
        if p not in self.f: self.f[p] = p
        elif p != self.f[p]:
            self.f[p] = self.find(self.f[p])
        return self.f[p]
    def union(self, p1, p2):
        if (f1 := self.find(p1)) < (f2 := self.find(p2)):   self.f[f2] = f1
        elif f2 < f1:   self.f[f1] = f2

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        uf = UnionFind()
        edges = []

        for row in range(m := len(heights)):
            for col in range(n := len(heights[0])):
                global_id = row * n + col
                if 0 <= row <= m - 2:
                    neighbor_id = global_id + n
                    heapq.heappush(edges, (abs(heights[row][col] - heights[row + 1][col]), global_id, neighbor_id))
                if 0 <= col <= n - 2:
                    neighbor_id = global_id + 1
                    heapq.heappush(edges, (abs(heights[row][col] - heights[row][col + 1]), global_id, neighbor_id))
        startID, endID = 0, len(heights) * len(heights[0]) - 1
        res = 0
        while uf.find(endID) != startID:
            e, p1, p2 = heapq.heappop(edges)
            uf.union(p1, p2)
            res = max(res, e)
        return res

        
