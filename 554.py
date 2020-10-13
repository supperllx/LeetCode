class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ct = collections.Counter()
        for row in wall:
            temp_sum = 0
            for i in range(len(row) - 1):
                temp_sum += row[i]
                ct[temp_sum] += 1
        return len(wall) - ct.most_common(1)[0][1] if len(ct) else len(wall)