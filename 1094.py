class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        s = set()
        d_start = collections.defaultdict(list)
        for t in trips:
            s.add(t[1])
            # s.add(t[2]) # don't need this cause we only care the loading location instead of unload location
            d_start[t[1]].append((t[2], t[0]))

        s = list(s)
        heapq.heapify(s)
        curTotal = 0
        hp = []

        while s:
            curLocation = heapq.heappop(s)
            while hp and hp[0][0] <= curLocation:
                curTotal -= heapq.heappop(hp)[1]
            for customer in d_start[curLocation]:
                heapq.heappush(hp, customer)
                curTotal += customer[1]
                if curTotal > capacity:
                    return False
        return True