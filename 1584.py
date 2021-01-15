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
    def minCostConnectPoints(self, points: List[List[int]]) -> int: # Kruskal
        # def dist(p1, p2):
        #     # return abs((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 )**0.5
        #     return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        uf = UnionFind()
        n_points = len(points)
        edges = []
        for i in range(n_points):
            for j in range(i + 1, n_points):
                p1, p2 = tuple(points[i]), tuple(points[j])
                edges.append((abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), i, j))
                # heapq.heappush(edges, (abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]), i, j))

        res = 0

        edges.sort()
        for e, p1, p2 in edges:
            if uf.find(p1) != uf.find(p2):
                uf.union(p1, p2)
                res += e

        # while edges:
        #     e, p1, p2 = heapq.heappop(edges)
        #     if uf.find(p1) != uf.find(p2):
        #         res += e
        #         uf.union(p1, p2)
        return res
            

        
