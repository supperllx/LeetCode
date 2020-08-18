class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None


    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.min = x
            self.stack.append(x - self.min)
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x


    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        else:
            x = self.stack[-1]
            if x >= 0:
                self.stack.pop()
                return x+self.min
            else:
                ans = self.min
                self.min -= x
                self.stack.pop()
                return ans


    def top(self) -> int:
        if len(self.stack) == 0:
            return None

        x = self.stack[-1]
        if x >= 0:
            return x+self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min