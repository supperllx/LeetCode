# class Solution:
#     def rotateString(self, A: str, B: str) -> bool:
#         if A == B:
#             return True
#         if len(A) != len(B):
#             return False
#         for i in range(len(A)):
#             A += A[i]
#             if A[i + 1:] == B:
#                 return True
#         return False

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        return len(A) == len(B) and B in (A + A)