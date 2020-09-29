"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            pre = Node(0)
            p = pre
            while cur:
                if cur.left:
                    p.next = cur.left
                    p = p.next
                if cur.right:
                    p.next = cur.right
                    p = p.next
                cur = cur.next
            cur = pre.next
        return root