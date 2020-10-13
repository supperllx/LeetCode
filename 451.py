class Solution:
    def frequencySort(self, s: str) -> str:
        ct = collections.Counter(s)
        res = ''
        for t in ct.most_common():
            for i in range(t[1]):   res += t[0]
        return res