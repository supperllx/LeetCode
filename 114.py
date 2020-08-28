# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import copy
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None:
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        root.left, root.right = root.right, root.left
        l_root = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = l_root