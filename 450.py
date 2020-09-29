# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root:
            if key < root.val:  root.left = self.deleteNode(root.left, key)
            elif key > root.val:    root.right = self.deleteNode(root.right, key)
            else:
                if (not root.left) and (not root.right):
                    root = None
                elif (not root.left) or (not root.right):
                    root = root.left if root.left else root.right
                else:
                    p = root.right
                    while p.left:   p = p.left
                    root.val = p.val
                    root.right = self.deleteNode(root.right, p.val)
            return root


