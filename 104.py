# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        res = 0
        def func(root, level):
            if root:
                nonlocal res
                res = max(res, level)
                func(root.left, level + 1)
                func(root.right, level + 1)
        func(root, 1)
        return res

# class Solution:
#     def maxDepth(self, root: TreeNode) -> int:
#         if root:
#             return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
#         else:
#             return 0