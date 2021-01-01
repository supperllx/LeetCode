class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # return max([sum(i) for i in accounts])
        res = 0
        for acnt in accounts:
            res = max(res, sum(acnt))
        return res