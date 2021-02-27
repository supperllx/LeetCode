class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        increase, decrease = False, False
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                increase = True
            elif A[i] > A[i + 1]:
                decrease = True
        return not (increase and decrease)
