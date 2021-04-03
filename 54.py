class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, n - 1
        top, bottom = 0, m - 1
        res = []
        while left <= right and top <= bottom:
            res += [matrix[top][i] for i in range(left, right + 1)]
            res += [matrix[j][right] for j in range(top + 1, bottom + 1)] # make sure we could fetch as much as possible in the first half part
            if left < right and top < bottom:
                res += [matrix[bottom][i] for i in range(right - 1, left - 1, -1)]
                res += [matrix[j][left] for j in range(bottom - 1, top, -1)]
            left += 1
            right -= 1
            top += 1
            bottom -= 1
        return res