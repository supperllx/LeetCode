class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        flag = 0
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        res = 0
        for k in d.keys():
            if d[k] % 2 == 0:
                res += d[k]
            else:
                res += (d[k] -1)
                flag = 1
        return res if flag == 0 else res+1