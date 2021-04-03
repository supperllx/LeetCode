class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        arr = list(s)
        for i in reversed(stack):
            del arr[i]
        return ''.join(arr)