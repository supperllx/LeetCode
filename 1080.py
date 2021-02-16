# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def func(root, lastSum):
            if root:
                if not root.left and not root.right:
                    if lastSum + root.val < limit:
                        return False
                    else:
                        return True
                else:
                    if not func(root.left, lastSum + root.val):
                        root.left = None
                    if not func(root.right, lastSum + root.val):
                        root.right = None
                    if not root.left and not root.right:
                        return False
                    else:
                        return True

        preNode = TreeNode(0)
        preNode.left = root
        func(preNode, 0)
        return preNode.left
