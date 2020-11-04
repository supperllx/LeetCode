# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        dq = collections.deque()
        dq.append(root)
        level = 0
        while len(dq):
            size = len(dq)
            last = -float('inf') if level % 2 == 0 else float('inf')
            for i in range(size):
                node = dq.popleft()
                if level % 2 == 0:
                    if node.val % 2 != 1 or node.val <= last:   return False
                else:
                    if node.val % 2 != 0 or node.val >= last:   return False
                if node.left:   dq.append(node.left)
                if node.right:  dq.append(node.right)
                last = node.val
            level += 1
        return True