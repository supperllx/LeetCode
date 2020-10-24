# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = 0
        def func(root, pre_val):
            if root:
                nonlocal res
                pre_val<<=1
                if not root.left and not root.right:
                    pre_val += root.val
                    res += pre_val
                else:
                    func(root.left, pre_val + root.val)
                    func(root.right, pre_val + root.val)
        func(root, 0)
        return res