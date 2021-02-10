class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        arr = [0] * n
        for i in range(n):
            arr[i] = abs(ord(s[i]) - ord(t[i]))
        
        res = 0
        curCost = 0
        left, right = 0, 0
        while right < n:
            curCost += arr[right]
            while curCost > maxCost:
                curCost -= arr[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
