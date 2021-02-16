class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        n = len(S)
        def func(p, path):
            nonlocal res
            if p == n:
                res.append(path)
            else:
                while p < n and S[p].isnumeric():
                    path += S[p]
                    p += 1
                if p == n:
                    res.append(path)
                    return
                func(p + 1, path + S[p])
                if S[p].isupper():
                    func(p + 1, path + S[p].lower())
                else:
                    func(p + 1, path + S[p].upper())
        func(0, '')
        return res