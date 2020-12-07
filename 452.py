class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        dq = collections.deque(sorted(points, key=lambda pos: (pos[1], pos[0])))
        res = 0
        while len(dq):
            arrow = dq.popleft()[1]
            res += 1
            while len(dq):
                if dq[0][0] <= arrow:   dq.popleft()
                else:   break
        return res
