# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
#         def get_l(root, res):
#             if root:
#                 if (not root.left) and (not root.right):
#                     res.append(root.val)
#                 else:
#                     get_l(root.left, res)
#                     get_l(root.right, res)
#                 return res
        
#         l1 = get_l(root1, [])
#         l2 = get_l(root2, [])
#         return l1 == l2

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def func(root, path):
            if root:
                if not root.left and not root.right:
                    path.append(root.val)
                else:
                    func(root.left, path)
                    func(root.right, path)
                return path
        return func(root1, []) == func(root2, [])