# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        else:
            l = self.isUnivalTree(root.left)
            r = self.isUnivalTree(root.right)
            l_val = root.left.val if root.left else root.val
            r_val = root.right.val if root.right else root.val
            return all([l, r, l_val == root.val, r_val == root.val])