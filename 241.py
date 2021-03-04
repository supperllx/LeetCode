class Solution:
    @functools.cache
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isnumeric():
            return [int(input)]
        else:
            ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
            res = []
            indexes = []
            for i, ch in enumerate(input):
                if ch in ops:
                    indexes.append(i)
            for i in indexes:
                for left in self.diffWaysToCompute(input[:i]):
                    for right in self.diffWaysToCompute(input[i+1:]):
                        res.append(ops[input[i]](left, right))
            return list(res)