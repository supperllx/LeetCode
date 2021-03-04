class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) < 2:
            return False
        ct = collections.Counter(deck)
        return reduce(math.gcd, ct.values()) >= 2