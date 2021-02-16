class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        n = len(A)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + A[i - 1]
        ct = collections.Counter()
        res = 0
        for nP in preSum:
            res += ct[nP]
            ct[nP + S] += 1
        return res