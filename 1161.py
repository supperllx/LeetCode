# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        dq = collections.deque()
        dq.append(root)
        level = 0
        max_sum = -float('inf')
        max_level = 0
        while dq:
            size = len(dq)
            level += 1
            level_sum = 0
            for _ in range(size):
                node = dq.popleft()
                level_sum += node.val
                if node.left:   dq.append(node.left)
                if node.right:  dq.append(node.right)
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

        return max_level
