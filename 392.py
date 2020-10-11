class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        for ch in s:
            while index < len(t):
                if t[index] == ch:  break
                index += 1
            if index >= len(t): return False
            index += 1
        return True