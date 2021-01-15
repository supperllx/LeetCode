class UnionFind:
    def __init__(self, n):
        self.n = n
        self.f = list(range(n))
    
    def find(self, x):
        if self.f[x] == x:  return x
        else:
            self.f[x] = self.find(self.f[x])
            return self.f[x]
    
    def union(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:    return 
        elif fx < fy:   self.f[fy] = fx
        else:   self.f[fx] = fy


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for i, j in pairs:
            uf.union(i, j)
        
        heapdict = collections.defaultdict(list)
        for index, ch in enumerate(s):
            fathter = uf.find(index)
            heapq.heappush(heapdict[fathter], ch)

        res = ''
        for i in range(len(s)):
            res += heapq.heappop(heapdict[uf.find(i)])
        return res