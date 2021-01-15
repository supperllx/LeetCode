class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def find(n):
            return n + 1 if n % 2 == 0 else n - 1
        
        res = 0
        for i in range(0, len(row), 2):
            p1 = row[i]
            p2 = find(p1)
            if row[i + 1] != p2:
                j = row.index(p2)
                row[i + 1], row[j] = row[j], row[i + 1]
                res += 1
        return res