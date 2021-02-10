class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        hp1, hp2 = list(s1), list(s2)
        heapq.heapify(hp1)
        heapq.heapify(hp2)
        while hp1 and hp2 and hp1[0] == hp2[0]:
            heapq.heappop(hp1)
            heapq.heappop(hp2)
        if hp1 and hp2: lastDiff = ord(heapq.heappop(hp1)) - ord(heapq.heappop(hp2))
        while hp1 and hp2:
            curDiff = ord(heapq.heappop(hp1)) - ord(heapq.heappop(hp2))
            if (lastDiff <= 0 and curDiff > 0) or (lastDiff >= 0 and curDiff < 0):
                return False
        return True