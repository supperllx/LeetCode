# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         dd = collections.defaultdict(list)
#         for edge in times:
#             dd[edge[0]].append((edge[1], edge[2]))

#         res = 0
#         dist = {node : float('inf') for node in range(1, n + 1)}

#         def func(node, timeusage):
#             nonlocal dist, res
#             if dist[node] > timeusage:
#                 dist[node] = timeusage
#                 if not dd[node]:
#                     res = max(res, timeusage)
#                 else:
#                     for nextNode, timecost in dd[node]:
#                         func(nextNode, timeusage + timecost)
        
#         func(k, 0)
#         maxTime = max(dist.values())
#         return maxTime if maxTime != float('inf') else -1

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int: # dijkstra
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        opening = [(0, k)]
        closed = set()
        dist = {node : float('inf') for node in range(1, n + 1)}
        dist[k] = 0
        while opening:
            curTime, curNode = heapq.heappop(opening)
            if curNode in closed:
                continue
            else:
                closed.add(curNode)
            for nextTime, nextNode in graph[curNode]:
                if nextNode not in closed:
                    if dist[nextNode] > curTime + nextTime:
                        dist[nextNode] = curTime + nextTime
                        heapq.heappush(opening, (dist[nextNode], nextNode))
        maxTime = max(dist.values())
        return maxTime if maxTime != float('inf') else -1