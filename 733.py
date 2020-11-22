# class Solution:  #DFS
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
#         height = len(image)
#         width = len(image[0])
#         old_color = image[sr][sc]

#         def dfs(row, col):
#             if image[row][col] == newColor: return 
#             else:
#                 image[row][col] = newColor
#                 if row > 0 and image[row - 1][col] == old_color:
#                     dfs(row - 1, col)
#                 if row < height - 1 and image[row + 1][col] == old_color:
#                     dfs(row + 1, col)
#                 if col > 0 and image[row][col - 1] == old_color:
#                     dfs(row, col - 1)
#                 if col < width - 1 and image[row][col + 1] == old_color:
#                     dfs(row, col + 1)
        
#         dfs(sr, sc)
#         return image

class Solution:  #BFS
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:   return image
        dq = collections.deque()
        dq.append((sr, sc))
        old_color = image[sr][sc]
        image[sr][sc] = newColor
        while len(dq):
            r, c = dq.popleft()
            if r > 0 and image[r - 1][c] == old_color:
                dq.append((r - 1, c))
                image[r - 1][c] = newColor
            if r < len(image) - 1 and image[r + 1][c] == old_color:
                dq.append((r + 1, c))
                image[r + 1][c] = newColor
            if c > 0 and image[r][c - 1] == old_color:
                dq.append((r, c - 1))
                image[r][c - 1] = newColor
            if c < len(image[0]) - 1 and image[r][c + 1] == old_color:
                dq.append((r, c + 1))
                image[r][c + 1] = newColor
        return image