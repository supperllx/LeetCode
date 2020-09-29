# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:    return []
        dq = collections.deque()
        dq.append(root)
        res = []
        is_rev = False
        while len(dq):
            size = len(dq)
            level = []
            for _ in range(size):
                node = dq.popleft()
                level.append(node.val)
                if node.left:   dq.append(node.left)
                if node.right:  dq.append(node.right)
            if is_rev:  level = level[::-1]
            res.append(level)
            is_rev = not is_rev
        return res
        