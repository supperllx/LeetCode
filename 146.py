class D_LinkNode:
    def __init__(self, v = None, k = None, pre = None, nxt = None):
        self.val = v
        self.key = k
        self.prev = pre
        self.next = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.cap = capacity
        self.head = D_LinkNode(0)
        self.tail = D_LinkNode(1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def get(self, key: int) -> int:
        if key not in self.d:    return -1
        else:
            node = self.d[key]
            self.refresh_node(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.val = value
            self.refresh_node(node)
        else:
            node = D_LinkNode(value, key)
            pre = self.tail.prev
            pre.next = node
            node.prev = pre
            self.tail.prev = node
            node.next = self.tail
            if self.length < self.cap:  self.length += 1
            else:
                h_node = self.head.next
                self.head.next = h_node.next
                h_node.next.prev = self.head
                self.d.pop(h_node.key)
            self.d[node.key] = node

    def refresh_node(self, node: D_LinkNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        pre = self.tail.prev
        pre.next = node
        node.prev = pre
        node.next = self.tail
        self.tail.prev = node




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)