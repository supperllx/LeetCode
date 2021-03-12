class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = collections.deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
        pos = [0, 0]
        for cmd in instructions:
            if cmd == 'G':
                pos[0] += directions[0][0]
                pos[1] += directions[0][1]
            elif cmd == 'L':
                directions.rotate(-1)
            else:
                directions.rotate(1)
        # return pos == [0, 0] or directions[0] != (0, 1)
        return not (pos != [0, 0] and directions[0] == (0, 1))