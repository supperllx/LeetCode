# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        res = 0
        def func(root):
            if not root:
                return 
            else:
                if root.left:
                    if (not root.left.left) and (not root.left.right):
                        nonlocal res
                        res += root.left.val
                    else:
                        func(root.left)
                func(root.right)
        func(root)
        return res