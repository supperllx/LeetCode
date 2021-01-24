class Solution:
    def maxProduct(self, words: List[str]) -> int:
        def s2int(s: str):
            d = set(s)
            res = 0
            for i in range(26):
                if chr(97 + i) in d:
                    res += 1
                res <<= 1
            return res
        
        dd = collections.defaultdict(int)
        for w in words:
            dd[key] = max(dd[(key := s2int(w))], len(w))
        
        arr = sorted(dd.items(), key = lambda v: v[1])
        res = 0
        for i in range(n := len(arr)):
            for j in range(i + 1, n):
                if arr[i][0] & arr[j][0] == 0:
                    res = max(res, arr[i][1] * arr[j][1])
        return res
