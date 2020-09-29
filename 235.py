# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         def get_path(root, n, path):
#             if root:
#                 path.append(root)
#                 if root.val < n:    get_path(root.right, n, path)
#                 elif root.val > n:  get_path(root.left, n, path)
#                 return path
#         pp = get_path(root, p.val, [])
#         pq = get_path(root, q.val, [])
#         n = min(len(pp), len(pq))
#         for i in range(n - 1):
#             if pp[i+1].val != pq[i+1].val:  return pp[i]
#         return pp[n - 1]

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if p.val > root.val and q.val > root.val: 
                return self.lowestCommonAncestor(root.right, p, q)
            elif p.val < root.val and q.val <root.val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return root