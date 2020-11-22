class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key = lambda pos: pos[0]**2 + pos[1]**2)
        return points[:K]
        