import copy
# class Solution:
#     def gameOfLife(self, board: List[List[int]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         origin = copy.deepcopy(board)
#         m, n = len(board), len(board[0])

#         for r in range(m):
#             for c in range(n):
#                 tempSum = 0
#                 for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1), (r - 1, c - 1), (r + 1, c - 1), (r - 1, c + 1), (r + 1, c + 1)):
#                     if 0 <= nr < m and 0 <= nc < n:
#                         tempSum += origin[nr][nc]
#                 if (board[r][c] == 1 and (tempSum < 2 or tempSum > 3)) or (board[r][c] == 0 and tempSum == 3):
#                     board[r][c] ^= 1

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                tempSum = 0
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1), (r - 1, c - 1), (r + 1, c - 1), (r - 1, c + 1), (r + 1, c + 1)):
                    if 0 <= nr < m and 0 <= nc < n and board[nr][nc] in (-1, 1):
                        tempSum += 1

                if board[r][c] == 1 and (tempSum < 2 or tempSum > 3):
                    board[r][c] = -1
                elif board[r][c] == 0 and tempSum == 3:
                    board[r][c] = 2
        for r in range(m):
            for c in range(n):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1