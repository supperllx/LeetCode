class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for i in S:
            if len(stack) == 0 or stack[-1] == i:   stack.append(i)
            else:
                if i == ')':    stack.pop()
                else:   stack.append(i)
        return len(stack)