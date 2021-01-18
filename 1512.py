class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ct = collections.Counter(nums)
        res = 0
        for n in ct.keys():
            res += ((ct[n] * (ct[n] - 1)) >> 1)
        return res