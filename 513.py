# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        d = {}
        max_level = 0
        def func(root, level):
            if root:
                nonlocal d, max_level
                if level in d:  d[level].append(root.val)
                else:   d[level] = [root.val]
                max_level = max(max_level, level)
                func(root.left, level + 1)
                func(root.right, level + 1)
        func(root, 0)
        return d[max_level][0]

