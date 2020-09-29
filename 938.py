# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
#         arr = []
#         def func(root):
#             if root:
#                 nonlocal arr
#                 func(root.left)
#                 arr.append(root.val)
#                 func(root.right)
#         func(root)
#         res = 0
#         for i in arr:
#             if i >= L and i <= R:
#                 res += i
#             if i > R:
#                 break
#         return res

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        def func(root):
            if root:
                if root.val >= L and root.val <= R:
                    nonlocal res
                    res += root.val
                func(root.left)
                func(root.right)
        func(root)
        return res