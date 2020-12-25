class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        hp = []
        n = len(matrix)
        for i in range(n):
            heapq.heappush(hp, (matrix[i][0], i, 0))
        res = 0
        while k:
            res = heapq.heappop(hp)
            if res[2] < n - 1:
                heapq.heappush(hp, (matrix[res[1]][res[2] + 1], res[1], res[2] + 1))
            k -= 1
        return res[0]