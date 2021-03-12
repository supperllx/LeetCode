class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda t: (t[1], t[0]))
        m = 0
        res = 1
        for n in range(1, len(pairs)):
            if pairs[m][1] < pairs[n][0]:
                res += 1
                m = n
        return res