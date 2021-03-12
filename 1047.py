# class Solution:
#     def removeDuplicates(self, S: str) -> str:
#         stack = []
#         for i in S:
#             if stack:
#                 if i == stack[-1]:
#                     stack.pop()
#                 else:
#                     stack.append(i)
#             else:
#                 stack.append(i)
#         return ''.join(stack)

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for ch in S:
            if not stack or stack[-1] != ch:
                stack.append(ch)
            else:
                while stack and stack[-1] == ch:
                    stack.pop()
        return ''.join(stack)