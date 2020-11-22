# class Solution:
#     def romanToInt(self, s: str) -> int:
#         d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
#         res = 0
#         stack = []
#         for ch in s:
#             if len(stack) == 0: stack.append(ch)
#             elif ch == 'V' and stack[-1] == 'I':
#                 stack.pop()
#                 res += 4
#             elif ch == 'X' and stack[-1] == 'I':
#                 stack.pop()
#                 res += 9
#             elif ch == 'L' and stack[-1] == 'X':
#                 stack.pop()
#                 res += 40
#             elif ch == 'C' and stack[-1] == 'X':
#                 stack.pop()
#                 res += 90
#             elif ch == 'D' and stack[-1] == 'C':
#                 stack.pop()
#                 res += 400
#             elif ch == 'M' and stack[-1] == 'C':
#                 stack.pop()
#                 res += 900
#             else:
#                 res += d[stack.pop()]
#                 stack.append(ch)
#         if len(stack):  res += d[stack[-1]]
#         return res

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500, 'M':1000}
        res = 0
        stack = []
        for ch in s:
            if len(stack) == 0: stack.append(ch)
            elif d[stack[-1]] < d[ch]:  res -= d[stack.pop()]
            else:   res += d[stack.pop()]
            stack.append(ch)
        res += d[stack[-1]]
        return res