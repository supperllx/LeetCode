class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-i for i in stones]
        heapq.heapify(hp)
        while len(hp) > 1:
            first = heapq.heappop(hp)
            second = heapq.heappop(hp)
            if (diff := (first - second)) != 0:
                heapq.heappush(hp, diff)
        return -hp[0] if len(hp) else 0