class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []
        self.length = 0



    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.length == 0:
            self.in_stack.append(x)
            self.length += 1
        else:
            if len(self.in_stack) == 0:
                for i in range(len(self.out_stack)):
                    self.in_stack.append(self.out_stack.pop())
                self.in_stack.append(x)
                self.length += 1
            else:
                self.in_stack.append(x)
                self.length += 1


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.length == 0:
            return None
        else:
            if len(self.out_stack) == 0:
                for i in range(len(self.in_stack)):
                    self.out_stack.append(self.in_stack.pop())
                self.length -= 1
                return self.out_stack.pop()
            else:
                self.length -= 1
                return self.out_stack.pop()



    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.length == 0:
            return None
        else:
            if len(self.out_stack) == 0:
                for i in range(len(self.in_stack)):
                    self.out_stack.append(self.in_stack.pop())
                return self.out_stack[-1]
            else:
                return self.out_stack[-1]



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return True if self.length == 0 else False

