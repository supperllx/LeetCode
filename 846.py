# import sortedcontainers
# class Solution:
#     def isNStraightHand(self, hand: List[int], W: int) -> bool:
#         n, r = divmod(len(hand), W)
#         if r != 0:
#             return False
#         # ct = collections.Counter(hand)
#         ct = sortedcontainers.SortedDict()
#         for card in hand:
#             if card not in ct:
#                 ct[card] = 1
#             else:
#                 ct[card] += 1
#         for _ in range(n):
#             start = min(ct)
#             for i in range(W):
#                 if (curNum := (start + i)) not in ct:
#                     return False
#                 else:
#                     ct[curNum] -= 1
#                     if ct[curNum] == 0:
#                         ct.pop(curNum)
#         return True

class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n, r = divmod(len(hand), W)
        if r != 0:
            return False
        ct = collections.Counter(hand)
        for _ in range(n):
            start = min(ct)
            for i in range(W):
                curNum = start + i
                if curNum not in ct:    return False
                else:
                    ct[curNum] -= 1
                    if ct[curNum] == 0: del ct[curNum]
        return True