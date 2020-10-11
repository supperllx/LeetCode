class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def func(s:str):
            res = [0] * len(s)
            d = {}
            for i in range(len(s)):
                if s[i] in d:   res[i] = d[s[i]]
                else:
                    res[i] = i
                    d[s[i]] = i
            return res

        return func(s) == func(t)