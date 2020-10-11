class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):    return False
        a = [0] * 26
        b = [0] * 26
        for ch in s:    a[ord(ch) - 97] += 1
        for ch in t:    b[ord(ch) - 97] += 1
        return a == b