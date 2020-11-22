class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odds = [i for i in A if i%2 == 1]
        evens = [i for i in A if i%2 == 0]
        res = []
        for _ in range(len(odds)):
            res.append(evens.pop())
            res.append(odds.pop())
        return res