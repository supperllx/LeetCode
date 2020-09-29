# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def maxPathSum(self, root: TreeNode) -> int:
#         max_res = -float('inf')
#         d = {}
#         def get_max_sub(root):
#             if root:
#                 nonlocal d
#                 if root in d:   return d[root]
#                 if (not root.left) and (not root.right):    d[root] = root.val
#                 else:   d[root] = root.val + max(0, get_max_sub(root.left), get_max_sub(root.right))
#                 return d[root]
#             else:   return 0

#         def func(root):
#             if root:
#                 nonlocal max_res
#                 temp = root.val + max(0, get_max_sub(root.left)) + max(0, get_max_sub(root.right))
#                 max_res = temp if temp > max_res else max_res
#                 func(root.left)
#                 func(root.right)
#         func(root)
#         return max_res
        
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -float('inf')
        def func(root):
            if root:
                nonlocal res
                l_max = func(root.left)
                r_max = func(root.right)
                res = max(res, root.val + l_max + r_max)
                return max(0, root.val + max(l_max, r_max))
            else:   return 0
        func(root)
        return res
                