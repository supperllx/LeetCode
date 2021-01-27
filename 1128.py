class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = collections.defaultdict(int)
        visited = set()
        for t in map(tuple, dominoes):
            d[t] += 1
        res = 0
        for i, j in dominoes:
            temp = 0
            if (t := (i, j)) not in visited:
                temp += d[t]
                visited.add((i, j))
                if i != j:
                    temp += d[(j, i)]
                    visited.add((j, i))
                res += (temp * (temp - 1) ) >> 1
                # print((i, j), temp)
        return res
