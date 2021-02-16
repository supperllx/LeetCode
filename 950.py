class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]: # reverse simulate
        deck.sort(reverse = True)
        dq = collections.deque()
        for n in deck:
            if not dq:
                dq.append(n)
            else:
                dq.appendleft(dq.pop())
                # dq.rotate(1)
                dq.appendleft(n)
        return list(dq)