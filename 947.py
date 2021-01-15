class UnionFind:
    def __init__(self):
        self.f = dict()
    def find(self, pos):
        if pos not in self.f:   self.f[pos] = pos
        elif self.f[pos] != pos:
            self.f[pos] = self.find(self.f[pos])
        return self.f[pos]
    def union(self, p1, p2):
        if (f1 := self.find(p1)) < (f2 := self.find(p2)):   self.f[f2] = f1
        elif f1 > f2:   self.f[f1] = f2

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind()
        n = len(stones)
        for i in range(n):
            for j in range(i+1, n):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    uf.union(i, j)
        
        dx = collections.defaultdict(list)
        dy = collections.defaultdict(list)

        for i, s in enumerate(stones):
            dx[s[0]].append(i)
            dy[s[1]].append(i)
        
        for samelist in dx.values():
            for i in range(len(samelist)):
                uf.union(samelist[0], samelist[i])
        for samelist in dy.values():
            for i in range(len(samelist)):
                uf.union(samelist[0], samelist[i])

        return n - len(set(uf.f.values()))
        
