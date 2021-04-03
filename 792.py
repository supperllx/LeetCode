class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dd = collections.defaultdict(list)
        for w in words:
            dd[w[0]].append(w)
        res = 0
        for ch in s:
            for i in range(len(dd[ch]) - 1, -1, -1):
                w = dd[ch][i]
                if w == ch:
                    res += 1
                else:
                    dd[w[1]].append(w[1:])
                del dd[ch][i]
        return res