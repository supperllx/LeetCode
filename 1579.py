class UnionFind:
    def __init__(self):
        self.d = dict()

    def find(self, x):
        if x not in self.d: #self.d[x] = x
            return x
        elif self.d[x] != x:
            self.d[x] = self.find(self.d[x])
        return self.d[x]
    
    def connect(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx < fy:
            # self.d[fx] = fx
            self.d[fy] = fx
        elif fx > fy:
            # self.d[fy] = fy
            self.d[fx] = fy

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf_1 = UnionFind()
        res = 0
        for e in filter(lambda x: x[0] == 3, edges): # for type 3
            if uf_1.find(e[1]) != uf_1.find(e[2]):
                uf_1.connect(e[1], e[2])
            else:   res += 1

        uf_2 = copy.deepcopy(uf_1) # copy for building Bob

        for t, u, v in filter(lambda x: x[0] == 1, edges): # for type 1 --> Alice
            if uf_1.find(u) != uf_1.find(v):
                uf_1.connect(u, v)
            else:   res += 1
        
        for t, u, v in filter(lambda x: x[0] == 2, edges): # for type 2 --> Bob
            if uf_2.find(u) != uf_2.find(v):
                uf_2.connect(u, v)
            else:   res += 1
        
        return res if len(uf_1.d) == n - 1 and len(uf_2.d) == n - 1 else -1
