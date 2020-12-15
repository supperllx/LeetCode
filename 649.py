# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         d = {'R': 'Radiant', 'D': 'Dire'}
#         dq = collections.deque(senate)
#         power = 0
#         while abs(power) < len(dq):
#             s = dq.popleft()
#             power += (1 if s == 'R' else -1)
#             if s == 'R' and power > 0:  dq.append(s)
#             elif s == 'D' and power < 0:    dq.append(s)
#         return d[dq[0]]

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dq = collections.deque(senate)
        power = 0
        while abs(power) < len(dq):
            sen = dq.popleft()
            power += (1 if sen == 'R' else -1)
            if sen == 'R' and power >= 1:   dq.append(sen)
            elif sen == 'D' and power <= -1:  dq.append(sen)
        return 'Radiant' if power > 0 else 'Dire'