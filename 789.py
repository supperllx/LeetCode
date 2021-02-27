class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def dist(pos):
            return abs(pos[0] - target[0]) + abs(pos[1] - target[1])
        # return dist([0,0]) < min(map(dist, ghosts))
        d = dist([0,0])
        for g in ghosts:
            if d >= dist(g):
                return False
        return True