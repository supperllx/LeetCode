class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        hp = []
        for num in range(lo, hi + 1):
            weight = 0
            x = num
            while x > 1:
                weight += 1
                if x % 2 == 1:
                    x = 3 * x + 1
                else:
                    x >>= 1
            heapq.heappush(hp, (weight, num))
        for i in range(k - 1):
            heapq.heappop(hp)
        return hp[0][1]
