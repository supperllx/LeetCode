class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) < 2:  return A
        p1, p2 = 0, 1
        while p2 < len(A):
            if A[p1] % 2 == 1:
                if A[p2] % 2 == 0:  
                    A[p1], A[p2] = A[p2], A[p1]
                    p1 += 1
                    p2 += 1
                else:   p2 += 1
            else:
                p1 += 1
                p2 += 1
        return A