# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         direction = [(1, 0), (1, 1)]
#         res = float('inf')

#         def dfs(row, col, temp):
#             if row == len(triangle) - 1:
#                 nonlocal res
#                 temp += triangle[row][col]
#                 res = min(res, temp)
#             else:
#                 for drow, dcol in direction:
#                     new_row = row + drow
#                     new_col = col + dcol
#                     if 0 <= new_col <= len(triangle[-1]) - 1:
#                         dfs(new_row, new_col, temp + triangle[row][col])
#         dfs(0, 0, 0)
#         return res


# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:
#         # draw the same triangle with the first value of each row in the raw triangle
#         dp = [[triangle[i][0]] * len(triangle[i]) for i in range(len(triangle))]

#         for row in range(1, len(triangle)):
#             # first element only need to add the last row's value
#             dp[row][0] += dp[row - 1][0]
#             # the last element of each row only have one available path
#             dp[row][-1] = dp[row - 1][-1] + triangle[row][-1]
            
#             for col in range(1, len(triangle[row]) - 1):
#                 temp = min(dp[row - 1][col - 1], dp[row - 1][col] )
#                 dp[row][col] = temp + triangle[row][col]
#         return min(dp[-1])

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for row in range(1, len(triangle)):
            triangle[row][0] += triangle[row - 1][0]
            triangle[row][-1] += triangle[row - 1][-1]
            for col in range(1, len(triangle[row]) - 1):
                triangle[row][col] += min(triangle[row - 1][col - 1], triangle[row - 1][col])
        return min(triangle[-1])

