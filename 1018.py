class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        n = 0
        for i in A:
            n = (n << 1) + i
            res.append(n%5 == 0)
        return res