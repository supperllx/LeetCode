# class Solution:
#     def fib(self, n: int) -> int:
#         @functools.cache
#         def fab(n):
#             if n == 0:  return 0
#             if n == 1:  return 1
#             return fab(n -1) + fab(n - 2)
#         return fab(n)

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:  return 0
        if n == 1:  return 1
        last1 = 0
        last2 = 1
        for i in range(2, n):
            last1, last2 = last2, last1 + last2
        return last1 + last2