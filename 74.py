class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:    return False
        row = 0
        col = len(matrix[0]) - 1
        while row <= len(matrix) - 1 and col >= 0:
            num = matrix[row][col]
            if target < num:    col -= 1
            elif target > num:  row += 1
            else:   return True
        return False