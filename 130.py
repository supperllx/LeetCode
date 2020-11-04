# class Solution:
#     def solve(self, board: List[List[str]]) -> None:  #DFS
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         if len(board) == 0: return []
#         nRow = len(board)
#         nCol = len(board[0])

#         def dfs(row, col):
#             nonlocal board, nRow, nCol
#             if row < 0 or row >= nRow or col < 0 or col >= nCol or board[row][col] != 'O':
#                 return
#             else:
#                 board[row][col] = 'C'
#                 dfs(row - 1, col)
#                 dfs(row + 1, col)
#                 dfs(row, col - 1)
#                 dfs(row, col + 1)
        
#         for row in range(nRow):
#             dfs(row, 0)
#             dfs(row, nCol - 1)
        
#         for col in range(nCol):
#             dfs(0, col)
#             dfs(nRow - 1, col)

#         for row in range(nRow):
#             for col in range(nCol):
#                 if board[row][col] == 'O':  board[row][col] = 'X'
#                 if board[row][col] == 'C':  board[row][col] = 'O'

class Solution:
    def solve(self, board: List[List[str]]) -> None:  #BFS
        if len(board) == 0: return []

        nRow = len(board)
        nCol = len(board[0])
        
        def bfs(row, col):
            nonlocal board, nRow, nCol
            if board[row][col] != 'O':  return
            dq = collections.deque()
            dq.append((row, col))
            board[row][col] = 'C'
            while len(dq):
                r, c = dq.popleft()
                if r > 0 and board[r - 1][c] == 'O':
                    dq.append((r - 1, c))
                    board[r - 1][c] = 'C'
                if r < nRow - 1 and board[r + 1][c] == 'O':
                    dq.append((r + 1, c))
                    board[r + 1][c] = 'C'
                if c > 0 and board[r][c - 1] == 'O':
                    dq.append((r, c - 1))
                    board[r][c - 1] = 'C'
                if c < nCol - 1 and board[r][c + 1] == 'O':
                    dq.append((r, c + 1))
                    board[r][c + 1] = 'C'
            
        for row in range(nRow):
            bfs(row, 0)
            bfs(row, nCol - 1)
        
        for col in range(nCol):
            bfs(0, col)
            bfs(nRow - 1, col)
        
        for row in range(nRow):
            for col in range(nCol):
                if board[row][col] == 'C':  board[row][col] = 'O'
                elif board[row][col] == 'O':  board[row][col] = 'X'
