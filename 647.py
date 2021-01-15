class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        def func(left, right):
            nonlocal res
            # temp = ''
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                # if left == right:   temp = s[left]
                # else:   temp = s[left] + temp + s[right]
                # res.add(temp)
                res += 1
                left -= 1
                right += 1

        for i in range(n):
            func(i, i)
            if i < n - 1:   func(i , i + 1)
        return res