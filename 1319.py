# class UnionFind:
#     def __init__(self, n):
#         self.f = dict([(i, i) for i in range(n)])
#     def find(self, p):
#         if p not in self.f: self.f[p] = p
#         elif p != self.f[p]:
#             self.f[p] = self.find(self.f[p])
#         return self.f[p]
#     def union(self, p1, p2):
#         if (f1 := self.find(p1)) < (f2 := self.find(p2)):   self.f[f2] = f1
#         elif f2 < f1:   self.f[f1] = f2

# class Solution:
#     def makeConnected(self, n: int, connections: List[List[int]]) -> int:
#         if len(connections) < n - 1:    return -1
#         uf = UnionFind(n)
#         # for i in range(n):
#         #     uf.union(i, i)
#         for i, j in connections:
#             uf.union(i, j)
#         s = set()
#         res = -1
#         for i in range(n):
#             if (f := uf.find(i)) not in s:
#                 res += 1
#                 s.add(f)
#         return res

class UnionFind:
    def __init__(self):
        self.f = dict()
    def find(self, x):
        if x not in self.f: self.f[x] = x
        elif self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx < fy:
            self.f[fy] = fx
        elif fx > fy:
            self.f[fx] = fy

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UnionFind()
        total_link = len(connections)
        total_need = n - 1
        if total_need > total_link: return -1
        nused = 0
        for x, y in connections:
            if uf.find(x) != uf.find(y):
                uf.union(x, y)
                nused += 1
        return total_need - nused

