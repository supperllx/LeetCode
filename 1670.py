class Node:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class FrontMiddleBackQueue:

    def __init__(self):
        self.preHead = Node()
        self.afterTail = Node()
        self.preHead.next, self.afterTail.prev = self.afterTail, self.preHead
        self.count = 0


    def pushFront(self, val: int) -> None:
        new_node = Node(val = val, prev = self.preHead, next = self.preHead.next)
        self.preHead.next = new_node
        new_node.next.prev = new_node
        self.count += 1


    def pushMiddle(self, val: int) -> None:
        p = self.preHead.next
        for _ in range(self.count // 2):
            p = p.next
        new_node = Node(val = val, prev = p.prev, next = p)
        p.prev.next, p.prev = new_node, new_node
        self.count += 1


    def pushBack(self, val: int) -> None:
        new_node = Node(val = val, prev = self.afterTail.prev, next = self.afterTail)
        self.afterTail.prev = new_node
        new_node.prev.next = new_node
        self.count += 1


    def popFront(self) -> int:
        if self.count == 0: return -1
        head = self.preHead.next
        self.preHead.next, head.next.prev = head.next, self.preHead
        self.count -= 1
        res = head.val
        del head
        return res


    def popMiddle(self) -> int:
        if self.count == 0: return -1
        p = self.preHead
        for _ in range(self.count // 2 if self.count % 2 == 0 else self.count // 2 + 1):
            p = p.next
        middle = p
        middle.prev.next, middle.next.prev = middle.next, middle.prev
        self.count -= 1
        res = middle.val
        del middle
        return res


    def popBack(self) -> int:
        if self.count == 0: return -1
        tail = self.afterTail.prev
        self.afterTail.prev, tail.prev.next = tail.prev, self.afterTail
        self.count -= 1
        res = tail.val
        del tail
        return res



# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()