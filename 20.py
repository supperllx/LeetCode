class Solution:
    def isValid(self, s: str) -> bool:
        left = {'(', '{', '['}
        right = {')': '(', '}': '{', ']': '['}
        stack = []
        for ch in s:
            if ch in left:
                stack.append(ch)
            elif not stack or right[ch] != stack.pop():
                return False
        return True if not stack else False