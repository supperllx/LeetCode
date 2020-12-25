class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        popped = popped[::-1]
        for n in pushed:
            stack.append(n)
            while len(stack) and len(popped):
                if stack[-1] == popped[-1]:
                    popped.pop()
                    stack.pop()
                else:
                    break
        return len(popped) == 0