# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         def get_d(root):
#             if root:
#                 return max(get_d(root.left), get_d(root.right)) + 1
#             else:
#                 return 0
#         res = 0
#         def func(root):
#             if root:
#                 nonlocal res
#                 distance = get_d(root.left) + get_d(root.right)
#                 res = distance if res < distance else res
#                 func(root.left)
#                 func(root.right)
#                 return res
#             else:   return 0
#         return func(root)

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 0
        def func(root):
            if not root:    return 0
            else:
                nonlocal res
                dl = func(root.left)
                dr = func(root.right)
                res = max(dl + dr, res)
                return max(dl, dr) + 1
        func(root)
        return res