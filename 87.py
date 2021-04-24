class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @functools.cache
        def func(i1, i2, length):
            if s1[i1: i1 + length] == s2[i2: i2 + length]:
                return True
            if collections.Counter(s1[i1: i1 + length]) != collections.Counter(s2[i2: i2 + length]):
                return False
            for j in range(1, length):
                if func(i1, i2, j) and func(i1 + j, i2 + j, length - j):
                    return True
                if func(i1, i2 + (length - j), j) and func(i1 + j, i2, length - j):
                    return True
            return False
        return func(0, 0, len(s1))