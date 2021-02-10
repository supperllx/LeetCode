class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = set()
        for down in range(2, n + 1):
            for up in range(1, down):
                gcd = math.gcd(up, down) # greatest common factor
                res.add('{0}/{1}'.format(up // gcd, down // gcd))
        return list(res)