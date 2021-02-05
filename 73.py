class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        def func(row, col):
            matrix[row] = [0] * n
            for r in range(m):
                matrix[r][col] = 0
        
        dq = collections.deque()
        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:   dq.append((r, c))
        
        while dq:
            row, col = dq.popleft()
            func(row, col)
        
