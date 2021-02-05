class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = collections.defaultdict(int) # contains the number of occurrence in the preSums
        d[0] = 1 # preSum[0] = 0, so d[0] at least has one record
        res = 0
        curSum = 0
        for n in nums:
            curSum += n
            res += d[curSum - k]
            d[curSum] += 1
        return res