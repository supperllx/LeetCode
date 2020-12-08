class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] = 0 if A[i][j] == 1 else 1
        
        for j in range(1, n):
            if sum([row[j] for row in A]) <= m / 2:
                for i in range(m):
                    A[i][j] = 0 if A[i][j] == 1 else 1

        res = 0
        for row in A:
            res += int(''.join([str(i) for i in row]), 2)
        return res