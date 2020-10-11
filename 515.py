# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:    return []
        res = []
        dq = collections.deque()
        dq.append(root)
        while len(dq):
            size = len(dq)
            temp_max = -float('inf')
            for _ in range(size):
                node = dq.popleft()
                temp_max = max(temp_max, node.val)
                if node.left:   dq.append(node.left)
                if node.right:  dq.append(node.right)
            res.append(temp_max)
        return res