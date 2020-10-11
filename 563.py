# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res = 0
        def func(root):
            if not root:    return 0
            else:
                nonlocal res
                l = func(root.left)
                r = func(root.right)
                res += abs(l - r)
                return root.val + l + r
        func(root)
        return res
        