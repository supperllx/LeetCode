class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while k > 0 and len(stack) and stack[-1] > n: 
                stack.pop()
                k -= 1
            stack.append(n)
        res = ''.join(stack[: -k]) if k > 0 else ''.join(stack)
        return '0' if len(res.lstrip('0')) == 0 else res.lstrip('0')