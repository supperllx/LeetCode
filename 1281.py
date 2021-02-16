class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        multi = 1
        s = 0
        for ch in str(n):
            multi *= int(ch)
            s += int(ch)
        return multi - s