# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:    return []
        res = []
        dq = collections.deque()
        dq.append(root)
        while len(dq):
            size = len(dq)
            for i in range(size):
                node = dq.popleft()
                if node.left:   dq.append(node.left)
                if node.right:  dq.append(node.right)
            res.append(node.val)
        return res