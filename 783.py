# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        if root:
            if root.left and root.right:
                min_l = min(abs(root.val - root.left.val), self.minDiffInBST(root.left))
                min_r = min(abs(root.val - root.right.val), self.minDiffInBST(root.right))
                return min(min_l, min_r)
            elif root.left and not root.right:
                min_l = min(abs(root.val - root.left.val), self.minDiffInBST(root.left))
                return min_l
            elif not root.left and root.right:
                min_r = min(abs(root.val - root.right.val), self.minDiffInBST(root.right))
                return min_r
            else:
                return float('inf')       

        else:
            return float('inf')