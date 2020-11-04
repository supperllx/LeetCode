class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ct = collections.Counter(magazine)
        for ch in ransomNote:
            if ct[ch] == 0: return False
            ct[ch] -= 1
        return True