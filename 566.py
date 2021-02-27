class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        res = [[0 for _ in range(c)] for _ in range(r)]
        if m * n != r * c:
            return nums
        for row in range(m):
            for col in range(n):
                global_id = row * n + col
                new_r, new_c = divmod(global_id, c)
                res[new_r][new_c] = nums[row][col]
        return res