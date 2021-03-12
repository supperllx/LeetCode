# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         lasfLen = len(s)
#         while True:
#             for i in range(26):
#                 s = ''.join(s.split(chr(97 + i) * k))
#             if len(s) == lasfLen:
#                 return s
#             else:
#                 lasfLen = len(s)

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
            else:
                stack[-1][1] += 1
            while stack and stack[-1][1] == k:
                stack.pop()
        res = ''
        for ch, n in stack:
            res += ch * n
        return res