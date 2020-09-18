"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return None
        d = {}
        p = head
        while p != None:
            d[p] = Node(x = p.val)
            p = p.next
        cur = head
        while cur != None:
            d[cur].next = d[cur.next] if cur.next != None else None
            d[cur].random = d[cur.random] if cur.random != None else None
            cur = cur.next
        return d[head]