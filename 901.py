class StockSpanner:

    def __init__(self):
        self.stack = []
        self.rec = {}
        self.i = 0

    def next(self, price: int) -> int:
        # print(price)
        if not self.stack:
            self.stack.append(price)
            self.rec[self.i] = 1
        else:
            if self.stack[-1] > price:
                self.stack.append(price)
                self.rec[self.i] = 1
            else:
                index = len(self.stack) - 1
                self.rec[self.i] = 1
                while index>=0 and self.stack[index] <= price:
                    self.rec[self.i] += self.rec[index]
                    index -= self.rec[index]
                self.stack.append(price)
        self.i += 1
        return self.rec[self.i - 1]
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)