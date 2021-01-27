class UnionFind:
    def __init__(self):
        self.d = dict()
    
    def find(self, x):
        if x not in self.d: self.d[x] = x
        elif self.d[x] != x:
            self.d[x] = self.find(self.d[x])
        return self.d[x]
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx < fy:   self.d[fy] = fx
        if fx > fy:   self.d[fx] = fy

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind()
        for e in filter(lambda e: e[1] == '=', equations):
            x, y = e[0], e[3]
            uf.union(x, y)

        for e in filter(lambda e: e[1] == '!', equations):
            x, y = e[0], e[3]
            if uf.find(x) == uf.find(y):    return False
        return True
