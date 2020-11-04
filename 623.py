# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        dq = collections.deque()
        dq.append(root)
        level = 1
        while len(dq):
            size = len(dq)
            for i in range(size):
                node = dq.popleft()
                if level == d - 1:
                    left = node.left
                    right = node.right
                    node.left = TreeNode(v)
                    node.right = TreeNode(v)
                    node.left.left = left
                    node.right.right = right
                if node.left:   dq.append(node.left)
                if node.right:  dq.append(node.right)
            if level == d - 1:   break
            level += 1
        return root