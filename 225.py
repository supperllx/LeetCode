from collections import deque

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        self.length = 0
        


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue.append(x)
        self.length += 1




    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.length == 0:
            return None
        else:
            for i in range(self.length - 1):
                head = self.queue.popleft()
                self.queue.append(head)

            self.length -= 1
            return self.queue.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        if self.length == 0:
            return None
        else:
            for i in range(self.length - 1):
                head = self.queue.popleft()
                self.queue.append(head)
            
            ans = self.queue[0]
            head = self.queue.popleft()
            self.queue.append(head)

            return ans


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if self.length == 0 else False
    
