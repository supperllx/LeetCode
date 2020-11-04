# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        res = 0
        def func(root, min_val, max_val):
            if root:
                nonlocal res
                min_val = min(min_val, root.val)
                max_val = max(max_val, root.val)
                res = max(res, max_val - min_val)
                func(root.left, min_val, max_val)
                func(root.right, min_val, max_val)
        func(root, float('inf'), -float('inf'))
        return res