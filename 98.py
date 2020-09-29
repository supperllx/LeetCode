# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         array = []
#         def func(root):
#             nonlocal array
#             if root != None:
#                 if root.left:
#                     func(root.left)
#                 array.append(root.val)
#                 if root.right:
#                     func(root.right)
#         func(root)
#         for i in range(len(array) - 1):
#             if array[i+1] <= array[i]:
#                 return False
#         return True

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def func(root, s, m):
            if not root:    return True
            else:
                return (s < root.val <m ) and(func(root.left, s, root.val)) and (func(root.right, root.val, m))
        return func(root, -float('inf'), float('inf'))