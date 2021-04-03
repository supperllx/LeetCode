class Solution:
    def rotatedDigits(self, N: int) -> int:
        d = {'0':'0', '1':'1', '8':'8', '2':'5', '5':'2', '6':'9','9':'6'}
        def func(n):
            rev_n = ''
            for i in str(n):
                if i not in d:  return False
                rev_n += d[i]
            if n != int(rev_n): return True
            else:   return False
        res = 0
        for n in range(2, N + 1):
            if func(n): res += 1
        return res            