class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:   return 0
        else:
            for ch in set(s):
                if s.count(ch) < k:
                    return max([self.longestSubstring(subS, k) for subS in s.split(ch)])
            return len(s)