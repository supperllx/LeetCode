class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        def func(i, path, k):
            if (n - i) > k * 3 or (n - i) < k * 1:  return # filter the too short or too long cases
            if i == n:
                if len(path) == 4:
                    nonlocal res
                    res.append('.'.join(path))
            else:
                for j in range(i, n):
                    cur = (s[i:j+1])
                    if cur == '0' or (cur.lstrip('0') == cur and 0 <= int(cur) <= 255):
                        func(j + 1, path + [cur], k - 1)
        func(0, [], 4)
        return res