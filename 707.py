class ListNode:
    def __init__(self, val = 0, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.preHead = ListNode()
        self.afterTail = ListNode()
        self.preHead.next, self.afterTail.prev = self.afterTail, self.preHead
        self.count = 0


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.count: return -1
        if index <= self.count // 2:
            p = self.preHead.next
            for _ in range(index):
                p = p.next
            return p.val
        else:
            n = self.count - 1
            p = self.afterTail.prev
            while n > index:
                p = p.prev
                n -= 1
            return p.val



    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = ListNode(val = val, prev = self.preHead, next = self.preHead.next)
        self.preHead.next.prev = new_head
        # new_head.next.prev = new_head
        self.preHead.next = new_head
        self.count += 1


    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_tail = ListNode(val = val, prev = self.afterTail.prev, next = self.afterTail)
        self.afterTail.prev.next = new_tail
        self.afterTail.prev = new_tail
        self.count += 1


    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:  self.addAtHead(val)
        elif index == self.count:   self.addAtTail(val)
        elif index < self.count:
            if index <= self.count // 2:
                p = self.preHead.next
                for _ in range(index):
                    p = p.next
            else:
                n = self.count - 1
                p = self.afterTail.prev
                while n > index:
                    p = p.prev
                    n -= 1
            node = ListNode(val = val, prev = p.prev, next = p)
            p.prev.next = node
            p.prev = node
            self.count += 1
            


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if 0 <= index < self.count:
            if index <= self.count // 2:
                p = self.preHead.next
                for _ in range(index):
                    p = p.next
            else:
                n = self.count - 1
                p = self.afterTail.prev
                while n > index:
                    p = p.prev
                    n -= 1
            
            p.prev.next, p.next.prev = p.next, p.prev
            self.count -= 1




# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)