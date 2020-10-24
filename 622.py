class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.capacity = k
        self.queue = [0] * k
        self.count = 0
        self.headIndex = 0
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.count == self.capacity: return False
        else:
            self.queue[(self.headIndex + self.count) % self.capacity] = value
            self.count += 1
            return True
        

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0: return False
        else:
            self.headIndex = (self.headIndex + 1) % self.capacity
            self.count -= 1
            return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0: return -1
        else:
            return self.queue[self.headIndex]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.count == 0: return -1
        else:
            return self.queue[(self.headIndex + self.count - 1) % self.capacity]
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()