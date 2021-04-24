# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def increasingBST(self, root: TreeNode) -> TreeNode:
#         array = []
#         def func(root):
#             if not root:
#                 return root
#             else:
#                 if root.left:
#                     func(root.left)
#                 array.append(root)
#                 if root.right:
#                     func(root.right)
#         func(root)
#         for i in range(len(array) -1):
#             array[i].right = array[i+1]
#             array[i].left = None
#         array[-1].right = None
#         array[-1].left = None
#         return array[0]

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        pre = TreeNode(0)
        cur = pre
        def func(root):
            if root:
                nonlocal cur
                func(root.left)
                cur.right = root
                root.left = None
                cur = cur.right
                func(root.right)
        func(root)
        return pre.right