class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        n_row, n_col = len(board), len(board[0])

        def func(r, c, p):
            if p == n - 1:  return board[r][c] == word[p]
            else:
                if board[r][c] != word[p]:  return False
                else:
                    temp_res = False
                    board[r][c] = ''
                    for dr, dc in directions:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < n_row and 0 <= new_c < n_col:
                            if func(new_r, new_c, p + 1):
                                temp_res = True
                                break
                    board[r][c] = word[p]
                    return temp_res
        
        for i in range(n_row):
            for j in range(n_col):
                if board[i][j] == word[0] and func(i, j, 0):    return True
        return False
