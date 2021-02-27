class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        ct = collections.Counter(filter(lambda x: len(x) <= 7, map(frozenset, words)))
        res = [0] * len(puzzles)

        for i, puz in enumerate(puzzles):
            CombsWithOutHead = list(map(lambda x: itertools.combinations(puz[1:], x), range(7))) # for combinations of puz[1:], so the length will be 0 ~ 6
            for comb in CombsWithOutHead:
                for c in comb:
                    res[i] += ct[frozenset(tuple(puz[0]) + c)]
        return res