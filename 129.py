# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        def func(root, pre_value):
            if root:
                if (not root.left) and (not root.right):
                    nonlocal res
                    res += (10 * pre_value + root.val)
                else:
                    func(root.left, (10 * pre_value) + root.val)
                    func(root.right, (10 * pre_value) + root.val)
        func(root, 0)
        return res