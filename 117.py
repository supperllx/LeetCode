"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root:    return None
#         dq = collections.deque()
#         dq.append((root, 0))
#         cur_level = -1
#         last = None
#         while len(dq):
#             temp = dq.popleft()
#             if temp[1] > cur_level:
#                 last = temp[0]
#                 cur_level = temp[1]
#             else:
#                 last.next = temp[0]
#                 last = temp[0]
#             if temp[0].left:    dq.append((temp[0].left, temp[1] + 1))
#             if temp[0].right:   dq.append((temp[0].right, temp[1] + 1))
#         return root

# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if not root:    return root
#         dq = collections.deque()
#         dq.append(root)
#         last = Node(0)
#         while len(dq):
#             size = len(dq)
#             for i in range(size):
#                 node = dq.popleft()
#                 if i == 0:
#                     last = node
#                 else:
#                     last.next = node
#                     last = node
#                 if node.left:   dq.append(node.left)
#                 if node.right:  dq.append(node.right)
#         return root

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur_level_node = root
        while cur_level_node != None:
            pre = Node(0)
            p = pre
            while cur_level_node != None:
                if cur_level_node.left:
                    p.next = cur_level_node.left
                    p = p.next
                if cur_level_node.right:
                    p.next = cur_level_node.right
                    p = p.next
                cur_level_node = cur_level_node.next
            cur_level_node = pre.next
        return root 

