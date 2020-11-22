class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for r in range(R):
            for c in range(C):
                res.append([r, c])
        res.sort(key = lambda pos:  abs(pos[0] - r0) + abs(pos[1] - c0))
        return res