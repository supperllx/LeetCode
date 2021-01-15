class unionFind:
    def __init__(self):
        self.f = dict()
    
    def find(self, u):
        if u in self.f:
            if self.f[u] == u:  return u
            else:
                self.f[u] = self.find(self.f[u])
                return self.f[u]
        else:
            self.f[u] = u
            return self.f[u]
    
    def union(self, u, v):
        if u not in self.f: self.f[u] = u
        if v not in self.f: self.f[v] = v
        fu, fv = self.f[u], self.f[v]
        if fu == fv:    return 0
        elif fu < fv:
            self.f[fv] = fu
        else:
            self.f[fu] = fv
        return 1

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = unionFind()
        for u, v in edges:
            if uf.find(u) == uf.find(v):    return [u, v]
            else:
                uf.union(u, v)
        
