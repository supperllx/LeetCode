class Solution:
    def customSortString(self, S: str, T: str) -> str:
        ct = collections.Counter(T)
        res = ''
        visited = set()
        for ch in S:
            if ch in ct and ch not in visited:
                res += ch * ct[ch]
                visited.add(ch)
        for ch in T:
            if ch not in visited:
                res += ch
        return res