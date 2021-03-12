class Solution:
    def partition(self, s: str) -> List[List[str]]:
        d = set()
        def func(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                d.add((left, right))
                left -= 1
                right += 1
        for i in range(len(s)):
            func(i, i)
            if i < len(s) - 1:
                func(i , i + 1)
        res = []
        def dfs(p, path):
            nonlocal res
            if p == len(s):
                res.append(path)
            for j in range(p, len(s)):
                if (p, j) in d:
                    dfs(j + 1, path + [s[p:j + 1]])
        dfs(0, [])
        return res