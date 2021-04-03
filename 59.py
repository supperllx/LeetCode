class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        res = [[0 for _ in range(n)] for _ in range(n)]
        n = 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                res[top][i] = n
                n += 1
            for i in range(top + 1, bottom + 1):
                res[i][right] = n
                n += 1
            if left < right and top < bottom:
                for i in range(right - 1, left - 1, -1):
                    res[bottom][i] = n
                    n += 1
                for i in range(bottom - 1, top, -1):
                    res[i][left] = n
                    n += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res