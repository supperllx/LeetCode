# class Solution:
#     def leastBricks(self, wall: List[List[int]]) -> int:
#         ct = collections.Counter()
#         for row in wall:
#             temp_sum = 0
#             for i in range(len(row) - 1):
#                 temp_sum += row[i]
#                 ct[temp_sum] += 1
#         return len(wall) - ct.most_common(1)[0][1] if len(ct) else len(wall)

# class Solution:
#     def leastBricks(self, wall: List[List[int]]) -> int:
#         ct = collections.Counter()
#         for row in wall:
#             temp = 0
#             for i in range(len(row) - 1):
#                 temp += row[i]
#                 ct[temp] += 1
#         return len(wall) - (ct.most_common(1)[0][1] if len(ct) else 0)

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        ct = collections.Counter()
        for row in wall:
            totalLength = 0
            for brickLength in row[:-1]:
                totalLength += brickLength
                ct[totalLength] += 1
        return len(wall) - (ct.most_common(1)[0][1] if ct else 0)