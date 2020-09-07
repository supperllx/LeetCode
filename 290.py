class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l_s = s.split(' ')
        d = {}
        values = set()
        if len(pattern) != len(l_s):
            return False
        for i in range(len(pattern)):
            p = pattern[i]
            w = l_s[i]
            if p not in d:
                if w in values:
                    return False
                else:
                    d[p] = w
                    values.add(w)
            else:
                if d[p] != w:
                    return False

        return True