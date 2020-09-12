class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = ''
        for i in S:
            if i == '(':
                if stack:
                    res += '('
                stack.append('(')
            else:
                stack.pop()
                if stack:
                    res += ')'
        return res
        