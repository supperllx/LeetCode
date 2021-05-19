class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @functools.cache
        def func(index: int, step: int)->int:
            if index < 0 or index >= arrLen or index > step: # if index > step, you will never be able to go back to 0
                return 0
            elif index <= 1 and step == 1:
                return 1
            else:
                step -= 1
                return func(index - 1, step) + func(index, step) + func(index + 1, step)
        return func(0, steps) % (10 ** 9 + 7)