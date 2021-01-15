class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:  return s
        def getLength(left, right):
            nonlocal s
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        
        res = ''
        max_length = 0
        for i in range(n - 1):
            s1 = getLength(i, i)
            s2 = getLength(i, i + 1)
            if len(s1) > max_length:
                res = s1
                max_length = len(s1)
            if len(s2) > max_length:
                res = s2
                max_length = len(s2)
        return res
            