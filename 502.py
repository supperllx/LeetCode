# class Solution:
#     def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
#         if W >= max(Capital):
#             return W + sum(heapq.nlargest(k, Profits))
        
#         pHp, cHp = [], []
#         for p, c in zip(Profits, Capital):
#             heapq.heappush(cHp, (c, p))
#         for _ in range(k):
#             while cHp and cHp[0][0] <= W:
#                 c, p = heapq.heappop(cHp)
#                 heapq.heappush(pHp, (-p, c))
#             if not pHp:
#                 break
#             else:
#                 W += (- heapq.heappop(pHp)[0])
#             while pHp:
#                 p, c = heapq.heappop(pHp)
#                 heapq.heappush(cHp, (c, -p))
#         return W

class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        if W >= max(Capital):
            return W + sum(heapq.nlargest(k, Profits))
        
        hp = []
        for p, c in zip(Profits, Capital):
            heapq.heappush(hp, (-p, c))
        for _ in range(k):
            if not hp:
                break
            temp = []
            while hp and hp[0][1] > W:
                # heapq.heappush(temp, heapq.heappop(hp))
                temp.append(heapq.heappop(hp))
            if hp:
                W += -heapq.heappop(hp)[0]
            else:
                break
            hp += temp
            heapq.heapify(hp)
        return W