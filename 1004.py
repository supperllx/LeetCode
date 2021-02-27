class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        curSum = 0
        Kremain = K
        left, right = 0, 0
        while right < len(A):
            curSum += 1
            if A[right] == 0:
                Kremain -= 1
            while Kremain < 0:
                if A[left] == 0:
                    Kremain += 1
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res
