# class Solution:
#     def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
#         m, n = len(matrix), len(matrix[0])
#         def bfs(r0, c0):
#             nonlocal matrix, m, n
#             dq = collections.deque()
#             visited = set()
#             dq.append((r0, c0))
#             visited.add((r0, c0))
#             dist = -1
#             while dq:
#                 dist += 1
#                 for _ in range(len(dq)):
#                     r, c = dq.popleft()
#                     if matrix[r][c] == 0:   return dist
#                     for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
#                         if (nr, nc) not in visited and 0 <= nr < m and 0 <= nc < n:
#                             dq.append((nr, nc))
#                             visited.add((nr, nc))
#             return -1
        
#         res = [[0 for _ in range(n)] for _ in range(m)]

#         for row in range(m):
#             for col in range(n):
#                 if matrix[row][col] != 0:
#                     res[row][col] = bfs(row, col)
#         return res

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        zeros = [(r, c) for r in range(m) for c in range(n) if matrix[r][c] == 0]
        visited = set(zeros)

        dq = collections.deque(zeros)
        while dq:
            r, c = dq.popleft()
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (nr, nc) not in visited and 0 <= nr < m and 0 <= nc < n:
                    res[nr][nc] = res[r][c] + 1
                    dq.append((nr, nc))
                    visited.add((nr, nc))
        return res