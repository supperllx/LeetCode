class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        p = 2
        while p < len(A):
            if (A[p-2] + A[p-1] > A[p] and A[p-2] + A[p] > A[p-1] and A[p-1] + A[p] > A[p-2]):
                return A[p-2] + A[p-1] + A[p]
            p += 1
        return 0
        