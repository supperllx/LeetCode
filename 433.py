class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank = set(bank)
        if end not in bank: return -1
        change = {'A':'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        dq = collections.deque()
        level = -1
        dq.append(start)
        while dq:
            level += 1
            for _ in range(len(dq)):
                curG = dq.popleft()
                if curG == end: return level
                for i, ch in enumerate(curG):
                    for mute in change[ch]:
                        nxtG = curG[:i] + mute + curG[i+1: ]
                        if nxtG in bank:
                            dq.append(nxtG)
        return -1