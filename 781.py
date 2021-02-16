class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res = 0
        ct = collections.Counter(answers)
        for num, count in ct.items():
            if num == 0:
                res += count
            else:
                if count % (num + 1) == 0:
                    res += count
                else:
                    res += (count // (num + 1) + 1) * (num + 1)
        return res