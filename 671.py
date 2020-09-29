# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def func(root):
            if (root.left != None) and (root.right != None):
                if max(root.right.val, root.left.val) > root.val:
                    return max(root.right.val, root.left.val)
                else:
                    return min(func(root.left), func(root.right))
            else:
                return -1
        return func(root)