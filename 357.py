class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n > 10:
            return 0
        ans = 10
        base = 9
        i = 9
        for _ in range(n - 1):
            base *= i
            ans = ans + base
            i -= 1
        return ans