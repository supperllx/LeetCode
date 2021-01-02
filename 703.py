class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = nums
        self.k = k
        heapq.heapify(self.hp)
        while len(self.hp) > k:
            heapq.heappop(self.hp)


    def add(self, val: int) -> int:
        # if len(self.hp) < self.k:
        #     heapq.heappush(self.hp, val)
        # else:
        #     heapq.heappushpop(self.hp, val)
        if len(self.hp) < self.k:
            heapq.heappush(self.hp, val)
        elif val > self.hp[0]:
            heapq.heapreplace(self.hp, val)

        return self.hp[0]        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)