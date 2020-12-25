class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:  return len(tasks)
        ct = collections.Counter(tasks)
        hp = []
        for k in ct.keys():
            heapq.heappush(hp, (-ct[k], k))
        res = []
        while len(hp):
            temp = []
            for _ in range(n + 1):
                temp.append(heapq.heappop(hp) if len(hp) else None)
            for t in temp:
                if t != None and t[0] < -1:
                    heapq.heappush(hp, (t[0] + 1, t[1]))
            res.extend(temp)
        while len(res):
            if not res[-1]: res.pop()
            else:   break
        return len(res)
