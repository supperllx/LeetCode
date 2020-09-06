class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        res = []
        p1 = 0
        p2 = 0
        temp = ''
        ans = 0
        while p2 < len(s):
            if s[p2] not in d:
                d.add(s[p2])
            else:
                ans = max(ans, p2 - p1)
                while s[p1] != s[p2]:
                    d.remove(s[p1])
                    p1 += 1
                p1 += 1
            p2 += 1

        return max(ans, p2 - p1)

