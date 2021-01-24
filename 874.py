class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = set(map(tuple, obstacles))
        cur = [0, 0]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        res = 0
        for cmd in commands:
            if cmd > 0:
                for i in range(cmd):
                    dx, dy = directions[d][0], directions[d][1]
                    if (cur[0] + dx, cur[1] + dy) in obs:   break
                    else:
                        cur[0] += dx
                        cur[1] += dy
                        res = max(res, cur[0]**2 + cur[1]**2)
            else:
                if cmd == -1:
                    d = (d + 1)%4
                elif cmd == -2:
                    d = (d - 1)%4
        return res

