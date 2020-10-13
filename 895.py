class FreqStack:

    def __init__(self):
        self.ct = collections.Counter()
        self.freq = collections.defaultdict(list)
        self.max_freq = 0
        

    def push(self, x: int) -> None:
        self.ct[x] += 1
        self.freq[self.ct[x]].append(x)
        self.max_freq = max(self.max_freq, self.ct[x])
        

    def pop(self) -> int:
        # max_freq = self.ct.most_common(1)[0][1]
        # res = self.freq[max_freq].pop()
        # self.ct[res] -= 1
        res = self.freq[self.max_freq].pop()
        if len(self.freq[self.max_freq]) == 0:   self.max_freq -= 1
        self.ct[res] -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()