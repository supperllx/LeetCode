# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        d = {}
        max_level = 0
        def func(root, level):
            if root:
                nonlocal max_level
                d[level] = d[level] + root.val if level in d else root.val
                max_level = max(max_level, level)
                func(root.left, level + 1)
                func(root.right, level + 1)
        func(root, 0)
        return d[max_level]