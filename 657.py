class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ct = collections.Counter(moves)
        return ct['U'] == ct['D'] and ct['L'] == ct['R']