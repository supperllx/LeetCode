import operator
class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 0:
            return None
        elif len(tokens) == 1:
            return int(tokens[0])
        else:
            ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
            stack = []
            # ans = None
            for i in tokens:
                if i not in ops:
                    stack.append(int(i))
                else:
                    # if ans == None:
                    #     right = int(stack.pop())
                    #     left = int(stack.pop())
                    #     print(left, ops[i], right)
                    #     ans = int(ops[i](left, right))
                    # else:
                    #     left = int(stack.pop())
                    #     print(left, ops[i], ans)
                    #     ans = int(ops[i](left, ans))

                    right = stack.pop()
                    left = stack.pop()
                    stack.append(int(ops[i](left, right)))
        return stack[0]

