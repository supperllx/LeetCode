class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        def func(s, path):
            nonlocal res
            if not s:
                if path:    res.append(path)
            else:
                for ch in d[s[0]]:
                    func(s[1:], path + ch)
        func(digits, '')
        return res

