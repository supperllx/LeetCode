# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def func(left, right):
            if (not left) and (not right):
                return True
            elif (not left) or (not right):
                return False
            elif left.val == right.val:
                return func(left.left, right.right) and func(left.right, right.left)
            else:
                return False
        return func(root.left, root.right) if root else True