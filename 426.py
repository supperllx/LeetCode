"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        arr = []
        def func(root):
            if root:
                nonlocal arr
                func(root.left)
                arr.append(root)
                func(root.right)
        func(root)
        n = len(arr)
        for i in range(n):
            arr[i].right = arr[(i + 1) % n]
            arr[i].left = arr[(i - 1) % n]
        return arr[0] if n else None

# class Solution:
#     def treeToDoublyList(self, root: 'Node') -> 'Node':  #TBD
#         if root:
#             p = root
#             l_head = self.treeToDoublyList(root.left)
#             r_head = self.treeToDoublyList(root.right)
#             root.right = r_head
#             while p.right:
#                 p, p.right.left = p.right, p
#             p.right = l_head
#             while p.right:
#                 p, p.right.left = p.right, p
#             p.right = root
#             root.left = p
#             return l_head