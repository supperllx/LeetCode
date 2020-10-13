"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head:
            left = self.flatten(head.child)
            right = self.flatten(head.next)
            head.next = left
            if left:    left.prev = head
            p = head
            while p.next:   p = p.next
            p.next = right
            if right:   right.prev = p
            head.child = None
            return head