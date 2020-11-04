# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         if len(intervals) == 0: return [newInterval]
#         res = []
#         for i in range(len(intervals)):
#             if not newInterval: 
#                 res.extend(intervals[i:])
#                 break
#             if intervals[i][1] < newInterval[0]:  res.append(intervals[i])
#             elif intervals[i][0] > newInterval[1]:
#                 res.append(newInterval)
#                 res.append(intervals[i])
#                 newInterval = None
#             else:
#                 newInterval[0] = min(intervals[i][0], newInterval[0])
#                 newInterval[1] = max(intervals[i][1], newInterval[1])
#         if newInterval: res.append(newInterval)
#         return res

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0: return [newInterval]
        res = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:  res.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                res.append(newInterval)
                res.extend(intervals[i:])
                newInterval = None
                break
            else:
                newInterval[0] = min(intervals[i][0], newInterval[0])
                newInterval[1] = max(intervals[i][1], newInterval[1])
        if newInterval: res.append(newInterval)
        return res
        