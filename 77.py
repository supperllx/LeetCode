class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def func(i, path):
            if len(path) == k:
                nonlocal res
                res.append(path)
            elif i <= n:
                for j in range(i, n + 1):
                    func(j + 1, path + [j])
        func(1, [])
        return res