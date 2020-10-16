# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def bstToGst(self, root: TreeNode) -> TreeNode:
#         array = []
#         def func(root):
#             if root:
#                 nonlocal array
#                 func(root.right)
#                 array.append(root)
#                 func(root.left)
#         func(root)
#         for i in range(1,len(array)):
#             array[i].val += array[i - 1].val
#         return root

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0
        def func(root):
            if root:
                nonlocal s
                func(root.right)
                root.val += s
                s = root.val
                func(root.left)
        func(root)
        return root
