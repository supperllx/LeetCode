# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        def func(root):
            if root:
                if root.val % 2 == 0:
                    nonlocal res
                    if (left := root.left):
                        if left.left:   res += left.left.val
                        if left.right:  res += left.right.val
                    if (right := root.right):
                        if right.left:  res += right.left.val
                        if right.right: res += right.right.val
                func(root.left)
                func(root.right)
        func(root)
        return res
