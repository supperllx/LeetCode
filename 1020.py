# class Solution:
#     def numEnclaves(self, A: List[List[int]]) -> int:
#         row = len(A)
#         col = len(A[0])
#         directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
#         def dfs(x, y, k):
#             # nonlocal A
#             if A[x][y] == 1:
#                 A[x][y] = k
#                 for dx, dy in directions:
#                     if 0 <= (new_x := x + dx) <= row - 1 and 0 <= (new_y := y + dy) <= col - 1:
#                         dfs(new_x, new_y, k)
        
#         for r in [0, row - 1]:
#             for c in range(col):
#                 if A[r][c] == 1:    dfs(r, c, 0)
#         for c in [0, col - 1]:
#             for r in range(row):
#                 if A[r][c] == 1:    dfs(r, c, 0)
        
#         res = 0
#         for r in range(1, row - 1):
#             for c in range(1, col - 1):
#                 if A[r][c] == 1:
#                     res += 1
#         return res

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        row = len(A)
        col = len(A[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        def bfs(x, y, k):
            dq = collections.deque()
            dq.append((x, y))
            A[x][y] = k
            while dq:
                cur_x, cur_y = dq.popleft()
                for dx, dy in directions:
                    if 0 <= (new_x := cur_x + dx) <= row - 1 and 0 <= (new_y := cur_y + dy) <= col - 1 and A[new_x][new_y] == 1:
                        A[new_x][new_y] = k
                        dq.append((new_x, new_y))
        
        for r in [0, row - 1]:
            for c in range(col):
                if A[r][c] == 1:    bfs(r, c, 0)
        for c in [0, col - 1]:
            for r in range(row):
                if A[r][c] == 1:    bfs(r, c, 0)
        
        res = 0
        for r in range(1, row - 1):
            for c in range(1, col - 1):
                if A[r][c] == 1:
                    res += 1
        return res

