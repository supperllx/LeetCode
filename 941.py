class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        left, right = 0, len(A) - 1
        while left < right and A[left] < A[left + 1]:    left += 1
        while right > left and A[right] < A[right - 1]:    right -= 1
        return left == right and left != 0 and right != len(A) - 1