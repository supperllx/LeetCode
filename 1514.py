class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float: # dijkstra
        graph = collections.defaultdict(list)
        for i, (x, y) in enumerate(edges):
            graph[x].append((succProb[i], y))
            graph[y].append((succProb[i], x))
        hp = [(-1.0, start)] # max heap
        visited = set()
        dist = collections.defaultdict(int)
        dist[start] = 1.0
        while hp:
            curNode = heapq.heappop(hp)
            curPr, iNode = -curNode[0], curNode[1]
            if iNode in visited:    continue
            visited.add(iNode)
            for nPr, iNeighbor in graph[iNode]:
                if iNeighbor not in visited:
                    if dist[iNeighbor] < curPr * nPr:
                        dist[iNeighbor] = curPr * nPr
                        heapq.heappush(hp, (-dist[iNeighbor], iNeighbor))
        return dist[end]
