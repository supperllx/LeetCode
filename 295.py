class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = [] # max heap
        self.right = [] # min heap
        self.median = None

    def addNum(self, num: int) -> None:
        if not self.median: heapq.heappush(self.right, num)
        else:
            if self.median > num:
                heapq.heappush(self.left, -num)
                while (len(self.left) - len(self.right)) > 0:
                    heapq.heappush(self.right, -heapq.heappop(self.left))
            else:
                heapq.heappush(self.right, num)
                while len(self.right) - len(self.left) > 1:
                    heapq.heappush(self.left, -heapq.heappop(self.right))
        self.median = (self.right[0] - self.left[0]) / 2 if len(self.left) == len(self.right) else self.right[0]
        

    def findMedian(self) -> float:
        return self.median
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()