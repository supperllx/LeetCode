class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m == 1 or n == 1:
            return 0
        hp = []
        visited = set()
        for i in range(m):
            heapq.heappush(hp, (heightMap[i][0], i, 0))
            # visited.add((i, 0))
            heapq.heappush(hp, (heightMap[i][n - 1], i, n - 1))
            # visited.add((i, n - 1))
        for j in range(n):
            heapq.heappush(hp, (heightMap[0][j], 0, j))
            # visited.add((0, j))
            heapq.heappush(hp, (heightMap[m - 1][j], m - 1, j))
            # visited.add((m - 1, j))
        
        res = 0
        while hp:
            h, r, c = heapq.heappop(hp)
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 < nr < m - 1 and 0 < nc < n - 1 and (nr, nc)  not in visited:
                    visited.add((nr, nc))
                    if h > heightMap[nr][nc]:
                        res += h - heightMap[nr][nc]
                    heapq.heappush(hp, (max(h, heightMap[nr][nc]), nr, nc))
        return res