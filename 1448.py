# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def func(root, path_max):
            nonlocal res
            if root:
                if root.val < path_max:
                    func(root.left, path_max)
                    func(root.right, path_max)
                else:
                    res += 1
                    func(root.left, root.val)
                    func(root.right, root.val)
        func(root, -float('inf'))
        return res