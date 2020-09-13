# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         def func(root):
#             if root == None:
#                 return root
#             else:
#                 root.left, root.right = func(root.right), func(root.left)
#                 return root
#         return func(root)

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root