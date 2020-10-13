# class Solution:
#     def dailyTemperatures(self, T: List[int]) -> List[int]:
#         stack = []
#         res = [0] * len(T)
#         for i in range(len(T)):
#             if len(stack) == 0 or T[stack[-1]] >= T[i]: stack.append(i)
#             else:
#                 while len(stack):
#                     if T[stack[-1]] < T[i]:
#                         last = stack.pop()
#                         res[last] = i - last
#                     else:   break
#                 stack.append(i)
#         return res

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i in range(len(T)):
            while len(stack) and T[stack[-1]] < T[i]:
                last = stack.pop()
                res[last] = i - last
            stack.append(i)
        return res

